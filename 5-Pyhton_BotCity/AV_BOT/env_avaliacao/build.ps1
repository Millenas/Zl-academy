$exclude = @("venv", "env_avaliacao.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "env_avaliacao.zip" -Force