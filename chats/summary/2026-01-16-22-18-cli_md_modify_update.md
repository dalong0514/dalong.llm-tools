# 操作总结

- 修改脚本新增 `--file` 入参，优先使用传入路径，否则回落到 `working/temp.md`。
- 读取文件后将处理结果写入剪贴板，不再回写原文件。
- 增加路径存在性校验，使用 `pathlib.Path` 处理文件路径。

## 影响文件
- `scripts/cli_md_modify.py`

## 测试
- 未运行测试。
