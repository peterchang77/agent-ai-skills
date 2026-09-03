# Headless Serving

Python's standard-library server is a useful zero-dependency way to view a local directory of HTML, Markdown, images, CSV files, and other generated artifacts. It is a convenience server, not a production web service.

## Local server

Serve a specific artifact directory rather than a broad home or project directory:

```bash
python3 -m http.server 8000 --directory /path/to/artifacts --bind 127.0.0.1
```

Visit `http://127.0.0.1:8000/`. The directory index provides a quick browser for files. HTML renders in the browser; Markdown is served as raw text unless a separate renderer is used.

Stop the foreground server with `Ctrl-C`. Choose another unused port if `8000` is occupied.

## Remote headless server: use an SSH tunnel

On the remote machine, bind only to loopback:

```bash
python3 -m http.server 8000 --directory /path/to/artifacts --bind 127.0.0.1
```

From the viewing machine, create a tunnel:

```bash
ssh -L 8000:127.0.0.1:8000 <user>@<remote-host>
```

Open `http://127.0.0.1:8000/` in the local browser. The remote server is not exposed directly to the remote network.

## Exposure and sensitive material

Do not bind to `0.0.0.0`, open firewall rules, expose a port through a proxy, or host artifacts publicly without explicit approval. The standard server does not provide authentication, authorization, HTTPS, audit logging, or production hardening.

Before serving, check the directory contents. A self-contained page can embed source data, images, annotations, identifiers, or secrets even when its filename looks harmless. Keep sensitive artifacts on approved storage, out of Git, and out of public/shared servers. Prefer a small authorized sample or a redacted derived page for demonstration.
