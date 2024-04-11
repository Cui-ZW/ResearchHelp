# Matlab绘图常见问题

## 输出时，JPG与EPS图片大小不一致
- 一般情况是输出eps时会默认裁剪空白导致图片大小不同，在print输出时，添加‘-loose’。