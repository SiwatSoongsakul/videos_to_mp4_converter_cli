import os
import subprocess
import concurrent.futures
from pathlib import Path
import typer
from typing import Optional
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.console import Console, Group
from rich.live import Live

app = typer.Typer()
console = Console()

def find_videos_from_path(path: str):
    try:
        path_obj = Path(path).resolve()
    except Exception as e:
        console.print(f'[bold red]X Failed Converting to Path: {e}')

    video_extensions = {'.mov', '.mkv', '.avi', '.wmv'}
    with console.status(f"[bold yellow]Scanning files in {path_obj}..."):
        try:
            if not(path_obj.exists() and path_obj.is_dir()): raise Exception('Cannot find giving path')

            videos = list()
            for file in path_obj.iterdir():
                if file.is_file() and file.suffix.lower() in video_extensions:
                    videos.append(file)

            if len(videos) == 0: raise Exception('Video Not found')
            console.print(f'[bold green]O[/bold green] Found {len(videos)} videos')

            return (path, videos)
        except Exception as e:
            console.print(f'[bold red]X Failed Finding Videos: {e}')
            raise typer.Exit(code=1)

def single_convert(vdo, output_dir, progress, task_id):
    output_file = output_dir / f'{vdo.stem}.mp4'

    commands = [
        'ffmpeg', '-i', str(vdo.resolve()),
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-c:a', 'aac', '-y', str(output_file)
    ]

    try:
        progress.update(task_id, description=f"[yellow]Converting: {vdo.name}", visible=True)
        subprocess.run(commands, check=True, capture_output=True)
        progress.update(task_id, description=f"[green]Done: {vdo.name}", completed=100)
    except FileNotFoundError:
        progress.console.print("[red]X Error: Cannot find 'ffmpeg' in the system")
        return
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode() if e.stderr else str(e)
        progress.console.print(f'[red]X Converting {vdo.name} Failed: {error_msg}')
    except Exception as e:
        progress.console.print(f'[red]X Unexpected Error with {vdo.name}: {e}')

def convert(output_dir: Path, videos):
    try:
        output_dir.mkdir(exist_ok = True)
        console.print(f'[bold green]O[/bold green] Create Destination Folder at {output_dir} ')
    except Exception as e:
        console.print(f'[bold red]X Failed Create Destination Folder: {e}')
        return
    
    max_usage = max(1, (os.cpu_count() or 2) // 2)
        
    progress = Progress(
        SpinnerColumn(), 
        TextColumn("[progress.description]{task.description}"),
        TaskProgressColumn(),
    )

    with Live(progress, refresh_per_second=10):
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_usage) as executor:
            futures = list()

            for vdo in videos:
                task_id = progress.add_task(f"[white]Waiting: {vdo.name}", total=100, visible=False)
                f = executor.submit(single_convert, vdo, output_dir, progress, task_id)
                futures.append(f)
            
            concurrent.futures.wait(futures)

@app.command()
def main(
    path: str = typer.Argument('.', help='Path of videos folder (. for current folder)'),
    out: str = typer.Option('converted-mp4', '--out', '-o', help='Destination folder name'),
):
    path_obj, videos = find_videos_from_path(path)
    if not videos:
        console.print('[bold red]X[/bold red] No videos found to convert')
        return
    output_dir = Path(str(path_obj) + '/' + str(out)).resolve()
    convert(output_dir, videos)

    console.print(f'\n[bold green]O[/bold green] Converted {len(videos)} videos Done!')

if __name__ == '__main__':
    app()