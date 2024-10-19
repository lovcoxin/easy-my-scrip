import requests

def wget(url, output_file=None):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        if output_file is None:
            output_file = url.split('/')[-1]  # 使用 URL 的最后一部分作为文件名

        with open(output_file, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"文件已下载并保存为 {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
