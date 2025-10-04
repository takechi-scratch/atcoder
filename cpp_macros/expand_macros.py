import os
import sys
import subprocess
from tempfile import NamedTemporaryFile
from pathlib import Path

if len(sys.argv) <= 1:
    print("ファイルパスを引数に指定してください")
    sys.exit(1)

submit_code_path = sys.argv[1]

with open(submit_code_path, "r", encoding="utf-8") as f:
    submit_code = f.read()

with open(Path(__file__).parent / "atcoder.h") as f:
    macro_code = f.read()

if '#include "../../cpp_macros/atcoder.h"' in submit_code:
    print("マクロを発見しました")
else:
    print("マクロが見つかりませんでした")

submit_code = submit_code.replace('#include "../../cpp_macros/atcoder.h"', macro_code)
print("マクロを置換しました")

with NamedTemporaryFile(mode="w", suffix=".cpp", delete=False) as tmpf:
    try:
        tmpf.write(submit_code)
        tmpf.flush()
        subprocess.run(["acc", "s", tmpf.name])
    finally:
        tmpf.close()
        os.unlink(tmpf.name)
