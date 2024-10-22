$exclude = @("venv", "bot_pagamentos.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_pagamentos.zip" -Force