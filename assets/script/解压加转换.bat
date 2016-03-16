pushd %~dp0
cd ../../artist/fla
for %%i in (*.fla) do winrar.exe x -y %%i %%~ni\
popd

python parsefla.py ../../artist/fla ../mc
python genindex.py
for /d %%f in (*.*) do rd %%f /s /q
pause