param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Arguments
)

# 获取当前脚本名称（不含扩展名）
$scriptName = [System.IO.Path]::GetFileNameWithoutExtension($MyInvocation.MyCommand.Definition)

# 构建Python脚本路径
$pythonScript = Join-Path -Path $PSScriptRoot -ChildPath "script\$scriptName.py"

# 检查Python脚本是否存在
if (-not (Test-Path -Path $pythonScript -PathType Leaf)) {
    Write-Error "Python script not found at: $pythonScript"
    exit 1
}

# 直接调用默认Python环境执行脚本
python $pythonScript @Arguments
exit $LASTEXITCODE