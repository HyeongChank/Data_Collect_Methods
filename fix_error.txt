가상환경 실행 오류 대처 방법

오류 내용
PS C:\Users\jsk38\git_clone\P3_Todolist\Flask_Server> & c:/Users/jsk38/git_clone/P3_Todolist/Flask_Server/venv/Scripts/Activate.ps1
& : 이 시스템에서 스크립트를 실행할 수 없으므로 C:\Users\js
k38\git_clone\P3_Todolist\Flask_Server\venv\Scripts\Activat
e.ps1 파일을 로드할 수 없습니다. 자세한 내용은 about_Execut 
ion_Policies(https://go.microsoft.com/fwlink/?LinkID=135170 
)를 참조하십시오.
위치 줄:1 문자:3
+ & c:/Users/jsk38/git_clone/P3_Todolist/Flask_Server/venv/ 
Scripts/Acti ...
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
~~~~~~~~~~~~
    + CategoryInfo          : 보안 오류: (:) [], PSSecurity 
Exc    eption
    + FullyQualifiedErrorId : UnauthorizedAccess


해결방법
-venv있는 폴더에서 정책 변경하고 다시 활성화 해야함
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

.\venv\Scripts\Activate.ps1
