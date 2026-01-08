import sys
import os
import asyncio

async def scan(host, port):
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=0.5
        )
        writer.close()
        await writer.wait_closed()
        return port
    except (asyncio.TimeoutError, OSError):
        return None

async def scan_host(host):
    ports = range(1, 1001)
    tasks = [scan(host, p) for p in ports]
    results = await asyncio.gather(*tasks)
    open_ports = [p for p in results if p]
    print(f"{host}: {open_ports}")

async def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file | ip | domain>")
        sys.exit(1)

    input_arg = sys.argv[1]   # filename OR host

    if os.path.isfile(input_arg):
        # File can be named ANYTHING
        with open(input_arg, "r") as f:
            for line in f:
                host = line.strip()
                if host:
                    await scan_host(host)
    else:
        host = input_arg
        await scan_host(host)

if __name__ == "__main__":
    asyncio.run(main())

