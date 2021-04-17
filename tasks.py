"""tasks.py"""
import invoke


@invoke.task
def api(ctx, dev=False):
    args = ["uvicorn", "fastapi_starter.main:app"]
    if dev:
        args.append("--reload")
    ctx.run(" ".join(args))
