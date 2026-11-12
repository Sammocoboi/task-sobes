import sys
import time
from urllib.request import urlopen


if len(sys.argv) != 2:
    print("проверка скорости", file=sys.stderr)
    raise SystemExit(2)

url = sys.argv[1]
total_bytes = 0
total_time = 0.0

try:
    for _ in range(10):
        started = time.perf_counter()
        downloaded = 0

        with urlopen(url, timeout=30) as response:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                downloaded += len(chunk)

        total_time += time.perf_counter() - started
        total_bytes += downloaded
except Exception as e:
    print(f"ошибка{e}")
    raise SystemExit(1)

print(f"Среднее время запроса: {total_time / 10:.3f} с")
print(f"Всего скачано: {total_bytes / 1_000_000:.3f} MB ({total_bytes} байт)")
print(f"Общее время: {total_time:.3f} с")
print(f"Средняя скорость скачивания: {total_bytes / 1_000_000 / total_time:.3f} MB/s")
