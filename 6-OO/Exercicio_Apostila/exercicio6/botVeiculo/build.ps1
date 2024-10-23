$exclude = @("venv", "botVeiculo.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "botVeiculo.zip" -Force