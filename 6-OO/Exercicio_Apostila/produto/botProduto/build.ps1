$exclude = @("venv", "botProduto.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "botProduto.zip" -Force