# Troubleshooting

## Common Issues

### Chrome 启动失败

**现象**: `Chrome 启动失败` 或 `Timeout` 错误

| 原因 | 解决方案 |
|------|---------|
| Chrome 未关闭 | 关闭所有 Chrome 窗口后重试 |
| Chrome 不在 PATH | 用 `--chrome-profile` 指定路径 |
| Profile 被锁定 | 删除 `User Data/Default/lockfile` |

### 登录状态丢失

**现象**: 页面跳转到登录页或显示无权限

- 确认已在 Chrome 正常登录 yunxuetang.cn
- 检查 Cookie 是否过期 (重新在浏览器中登录)
- 尝试手动访问课程页面确认登录状态

### 视频录制失败

**现象**: `captureStream blocked` 错误

- 某些 DRM 实现会阻止 `captureStream()`, 这是极少数情况
- 确认 Chrome 是最新版本
- 尝试重启脚本

**现象**: 录制数据为空 (0 chunks)

- 确认视频已开始播放 (检查是否需要手动点击播放)
- 检查网络连接是否正常
- 查看 `debug_*.png` 截图了解页面状态

### 文档页面图片为 0

**现象**: `未捕获到图片 URL`

- 该课程可能实际是视频 (API 类型标签不准)
- 脚本会自动尝试 video 和 doc 两种 URL
- 如仍失败, 手动在浏览器中打开课程确认内容类型

### WebM → MP4 转换失败

**现象**: `MP4 转换失败, 保留 WebM`

```bash
pip install imageio-ffmpeg
```

或安装系统 ffmpeg:
- Windows: `winget install ffmpeg`
- macOS: `brew install ffmpeg`

### 批量下载中断

**现象**: 脚本意外退出

- 进度已保存在 `download_progress.json`, 重新运行相同命令即可续传
- 已完成的课程会自动跳过

## 日志关键字速查

| 日志关键字 | 含义 |
|-----------|------|
| `[SKIP]` | 文件已存在, 跳过下载 |
| `[类型] 视频` | 检测到 m3u8 流, 将录制视频 |
| `[类型] 文档` | 检测到页面图片, 将生成 PDF |
| `[录制]` | MediaRecorder 正在录制 |
| `进度: X/Ys (Z%)` | 视频录制进度 |
| `[OK]` | 下载/转换成功 |
| `[ERR]` | 错误 |
