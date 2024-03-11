<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<ScanConfiguration Version="9.5">
  <SessionManagement Version="1.2">
    <SessionManagementMode>Manual</SessionManagementMode>
    <AllowConcurrentLogins>True</AllowConcurrentLogins>
    <AWSIdentityDetectedInLogin>False</AWSIdentityDetectedInLogin>
    <UseAutomaticABL>False</UseAutomaticABL>
    <inSessionDomTexts>
      <inSessionDomText>身份管理系统</inSessionDomText>
      <inSessionDomText>12px（默认）</inSessionDomText>
      <inSessionDomText>身份管理系统</inSessionDomText>
      <inSessionDomText>12px（默认）</inSessionDomText>
    </inSessionDomTexts>
    <ValidAblLogin>False</ValidAblLogin>
    <AutomaticLoginValidated>True</AutomaticLoginValidated>
    <RecordedSessionRequests>
      <request scheme="http" host="192.168.13.159" path="/sys/dictData/page/loginType" port="20086" method="GET" RequestEncoding="28591" IsBodyEngineFiltered="False" IsWebSocket="False" SessionRequestType="Login" ordinal="363" ValidationStatus="None" MultiStepTested="true" sequencePlaybackRequired="true">
        <raw encoding="none">GET /sys/dictData/page/loginType HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Referer: http://192.168.13.159:20086/udaam-ui/login?redirect=%2Fhome
Connection: keep-alive
Host: 192.168.13.159:20086
Content-Length: 0
Accept: application/json, text/plain, */*
Authorization: Basic Y2xpZW50SWQ6Y2xlbnRfc2VjcmV0
Accept-Language: en-US

</raw>
        <response status="200" bodyEncoding="utf-8">
          <body value="UEsDBBQAAAAIAG2PW1WehbvTZgEAAH8FAAAEACQAZGF0YQoAIAAAAAAAAQAYAFAUQ8zq6dgBUBRDzOrp2AFQFEPM6unYAeWSsU7DMBCGXwV5biXbcWwnG6IMCAGCAgtCyLEdFClto9gZqqpDFwSIgbVTYQUhHoCBl4GWvgUObSliqlQxAOP9999/9qfrANlSGoQYwgowVtjCTIuGNkacuhYYnl+/Xg5ABdjEiVY0MidiiHEVwSpmK4iFPg994hxKWAHCow5IlPPEkhDKPI9ElCCkVQA5gRBKHEgOpWTlQCLtpm47c32rfrK2U1ufiociLcrlqNzbzvRGGYipH0gSyUjwiMKICx6wmEMUMxwxj3LnNa3cghC5EG1knmQ2aTXd5Gjw8PJ8O767envsjW56o/7TuH/m7Imp6VgUqZ2umiH4KGSuhdX77tcgbBZpOlMOjM7L93zXtsXcWWTqcxZRSjnFmHiwJDtpzUIABF+lSQYwRabzVdVImqBbmeP0MY7xQjh3936Q5vDi/tdCVL6HFGIkiNU/v0k/YIxzvixOQjCCC+H8ize5DMTj7jtQSwECLQAUAAAACABtj1tVnoW702YBAAB/BQAABAAkAAAAAAAAAAAAAAAAAAAAZGF0YQoAIAAAAAAAAQAYAFAUQ8zq6dgBUBRDzOrp2AFQFEPM6unYAVBLBQYAAAAAAQABAFYAAACsAQAAAAA=" compressedBinaryValue="true" />
          <headers value="HTTP/1.1 200 OK&#xA;Content-Length: 1407&#xD;&#xA;Server: nginx&#xD;&#xA;X-Frame-Options: DENY&#xD;&#xA;X-Content-Type-Options: nosniff&#xD;&#xA;Expires: 0&#xD;&#xA;X-XSS-Protection: 1; mode=block&#xD;&#xA;Connection: keep-alive&#xD;&#xA;Vary: Origin&#xD;&#xA;Vary: Access-Control-Request-Method&#xD;&#xA;Vary: Access-Control-Request-Headers&#xD;&#xA;Date: Thu, 27 Oct 2022 09:58:54 GMT&#xD;&#xA;Content-Type: application/json&#xD;&#xA;Pragma: no-cache&#xD;&#xA;Cache-Control: no-cache, no-store, max-age=0, must-revalidate&#xD;&#xA;" />
        </response>
        <sessionCookies />
      </request>
      <request scheme="http" host="192.168.13.159" path="/sys/dictData/page/systemSettings" port="20086" method="GET" RequestEncoding="28591" IsBodyEngineFiltered="False" IsWebSocket="False" SessionRequestType="Login" ordinal="364" ValidationStatus="None" MultiStepTested="true" sequencePlaybackRequired="true">
        <raw encoding="none">GET /sys/dictData/page/systemSettings HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Referer: http://192.168.13.159:20086/udaam-ui/login?redirect=%2Fhome
Connection: keep-alive
Host: 192.168.13.159:20086
Content-Length: 0
Accept: application/json, text/plain, */*
Authorization: Basic Y2xpZW50SWQ6Y2xlbnRfc2VjcmV0
Accept-Language: en-US

</raw>
        <response status="200" bodyEncoding="utf-8">
          <body value="UEsDBBQAAAAIAG2PW1Ug6hsd6AEAAIkEAAAEACQAZGF0YQoAIAAAAAAAAQAYAFAUQ8zq6dgBUBRDzOrp2AFQFEPM6unYAc2TQWvbMBiG/8rQrkksybYs+RZIYGUsKYm7MsYIsix3BicxlnwopRDYpetlgR3WwkrZZfS23TZYf87s0X8xOUm31qct7LCj3u/V6+97PvkIiHkkgY8hbAGluS7U5jCVSvEDUwLVybI8vQQtoBMjaj7NjIghxm0E29h7gDzfZT5GxhFxzYH//AgkkfHIiDIpXA/FksqIOwI5jNoEiogxjBCrLyRCP5aHxjx+Ng76Tya73SDojwab0lOeFnULdv31w0zu1LGYuEw4oQg5DQkMKafMiylEsYdDzybUeNU818BnJkQqkSeZTuYzc/Pm3VV18qW6+lBevzGuRPVkzIvUWEHd/e38q4PIJdcyMCMDHxEHQtch1JCBt6U9JfNVP7/dtTTg9Q3Ao2kyM4Uii+7EEEIJxo69ilmXfsVAcFfaxKgik3l3lXXc+iOsGN7DOtztDybdveBRgyjciihtEq3OPpXLj9Xrt+X1orp4dXO+3IIrZeR/4BqHZn5JXJt5MGKQxiEXSDiMU4e6th3f49obDkeT/Z1Bb7g/6fZG/fG4Afil1plvWYjhDiK0g+wOMn8JgpDaVi4PDL7MIOVpu0ish9ZW20DNbfz4dvn962L9ysv3n8uLxd9sY1akaXMJTW2Nb63+wxW8OP4JUEsBAi0AFAAAAAgAbY9bVSDqGx3oAQAAiQQAAAQAJAAAAAAAAAAAAAAAAAAAAGRhdGEKACAAAAAAAAEAGABQFEPM6unYAVAUQ8zq6dgBUBRDzOrp2AFQSwUGAAAAAAEAAQBWAAAALgIAAAAA" compressedBinaryValue="true" />
          <headers value="HTTP/1.1 200 OK&#xA;Content-Length: 1161&#xD;&#xA;Server: nginx&#xD;&#xA;X-Frame-Options: DENY&#xD;&#xA;X-Content-Type-Options: nosniff&#xD;&#xA;Expires: 0&#xD;&#xA;X-XSS-Protection: 1; mode=block&#xD;&#xA;Connection: keep-alive&#xD;&#xA;Vary: Origin&#xD;&#xA;Vary: Access-Control-Request-Method&#xD;&#xA;Vary: Access-Control-Request-Headers&#xD;&#xA;Date: Thu, 27 Oct 2022 09:59:21 GMT&#xD;&#xA;Content-Type: application/json&#xD;&#xA;Pragma: no-cache&#xD;&#xA;Cache-Control: no-cache, no-store, max-age=0, must-revalidate&#xD;&#xA;" />
        </response>
        <sessionCookies />
      </request>
      <request scheme="http" host="192.168.13.159" path="/sys/authorization/oauth/token" port="20086" method="POST" RequestEncoding="28591" IsBodyEngineFiltered="False" IsWebSocket="False" SessionRequestType="Login" ordinal="365" ValidationStatus="None" MultiStepTested="true" sequencePlaybackRequired="true">
        <raw encoding="none">POST /sys/authorization/oauth/token HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Referer: http://192.168.13.159:20086/udaam-ui/login?redirect=%2Fhome
Connection: keep-alive
Host: 192.168.13.159:20086
Content-Length: 725
Accept: application/json, text/plain, */*
Origin: http://192.168.13.159:20086
Authorization: Basic Y2xpZW50SWQ6Y2xlbnRfc2VjcmV0
Accept-Language: en-US
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryVGFtaVi0vabwddzE

------WebKitFormBoundaryVGFtaVi0vabwddzE
Content-Disposition: form-data; name="grant_type"

password
------WebKitFormBoundaryVGFtaVi0vabwddzE
Content-Disposition: form-data; name="username"

superAdmin
------WebKitFormBoundaryVGFtaVi0vabwddzE
Content-Disposition: form-data; name="code"

5264
------WebKitFormBoundaryVGFtaVi0vabwddzE
Content-Disposition: form-data; name="orgId"


------WebKitFormBoundaryVGFtaVi0vabwddzE
Content-Disposition: form-data; name="secret"

Ce34IbbjTWHrf21522Bvd8rZPPQ9ZSJh/FjknSJ/xCJKwqfA8uD7H6gwp3I9t13I38cq9HiY0mptROsB/1U8XA==
------WebKitFormBoundaryVGFtaVi0vabwddzE
Content-Disposition: form-data; name="key"

1666864735870
------WebKitFormBoundaryVGFtaVi0vabwddzE--
</raw>
        <parameter name="grant_type" captureIndex="0" value="password" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="grant_type" />
        <parameter name="username" captureIndex="0" value="superAdmin" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="username" />
        <parameter name="code" captureIndex="0" value="5264" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="code" />
        <parameter name="orgId" captureIndex="0" value="" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="orgId" />
        <parameter name="secret" captureIndex="0" value="Ce34IbbjTWHrf21522Bvd8rZPPQ9ZSJh/FjknSJ/xCJKwqfA8uD7H6gwp3I9t13I38cq9HiY0mptROsB/1U8XA==" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="secret" />
        <parameter name="key" captureIndex="0" value="1666864735870" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="key" />
        <response status="200" bodyEncoding="utf-8">
          <body value="UEsDBBQAAAAIAG2PW1XhgPemNQEAALIBAAAEACQAZGF0YQoAIAAAAAAAAQAYAFAUQ8zq6dgBUBRDzOrp2AFQFEPM6unYAT2QTWrDMBCF76K1DZLl+Ce7/kG7KIYkbckqjKRxbJJIxpahJmRfuuoNerr2HB0loVppRu97M09Hpp1BNk84j9jgwY/DtTjgMMCWntjvx9fP5zeLmG+p6eHQsfmRTQh9kCYJaZ31zSvsR5ILfq2JrO5W1e3DglADU1U/X9pJfq3XZwsZpp3rN8QdUavHl8Xy/mZNWONGUggCDq0dPdnPStoTtbOGjETELFgXbuQSTsR00zvr9m47hS017NEa6FdTF6K0gysyLsi5JZ49LSt2OoXpHoIatKbUG+92aOk5rVWS8dLEnKcmTrNcx6quizjneYmiVFBIHr4lyDf+MkFRJuyp22Pd49D8myWqVgpMHuusJjMpTQxCYixnAlWqRYoqIQzfu5a4TUtMkckyxNXubA1dR9v+AVBLAQItABQAAAAIAG2PW1XhgPemNQEAALIBAAAEACQAAAAAAAAAAAAAAAAAAABkYXRhCgAgAAAAAAABABgAUBRDzOrp2AFQFEPM6unYAVAUQ8zq6dgBUEsFBgAAAAABAAEAVgAAAHsBAAAAAA==" compressedBinaryValue="true" />
          <headers value="HTTP/1.1 200 &#xA;Connection: keep-alive&#xD;&#xA;X-XSS-Protection: 1; mode=block&#xD;&#xA;Server: nginx&#xD;&#xA;Pragma: no-cache&#xD;&#xA;Content-Length: 434&#xD;&#xA;X-Frame-Options: DENY&#xD;&#xA;X-Content-Type-Options: nosniff&#xD;&#xA;Cache-Control: no-cache, no-store, max-age=0, must-revalidate&#xD;&#xA;Date: Thu, 27 Oct 2022 09:59:21 GMT&#xD;&#xA;Expires: 0&#xD;&#xA;Content-Type: application/json;charset=UTF-8&#xD;&#xA;" />
        </response>
        <sessionCookies />
      </request>
      <request scheme="http" host="192.168.13.159" path="/sys/system/udSystem/getSystemIdByCode" port="20086" method="GET" RequestEncoding="28591" IsBodyEngineFiltered="False" IsWebSocket="False" SessionRequestType="Login" ordinal="366" ValidationStatus="None" MultiStepTested="true" sequencePlaybackRequired="true">
        <raw encoding="none">GET /sys/system/udSystem/getSystemIdByCode?code=udaam HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Referer: http://192.168.13.159:20086/udaam-ui/login?redirect=%2Fhome
Connection: keep-alive
Host: 192.168.13.159:20086
Content-Length: 0
Accept: application/json, text/plain, */*
Authorization: Bearer 4fb2609d-004d-467c-bff8-7079e19ba830
Accept-Language: en-US

</raw>
        <parameter name="code" captureIndex="0" value="udaam" type="QUERY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="code" />
        <response status="200" bodyEncoding="utf-8">
          <body value="UEsDBBQAAAAIAG2PW1W3CEnMawAAAHgAAAAEACQAZGF0YQoAIAAAAAAAAQAYAFAUQ8zq6dgBUBRDzOrp2AFQFEPM6unYAS2KOw7CMAxAr4I8t5Jjy7jNbRySIoYKpJgJsSMmbsDp6DnqgfF9HnC61gaZEAfobn7vf1hb73aOBNvr83t/YQC/hHRbbyEJicaEI+khaZY5U4qjmlvEsiysSiazFmZkFZ6EU8F6lDZVhucOUEsBAi0AFAAAAAgAbY9bVbcIScxrAAAAeAAAAAQAJAAAAAAAAAAAAAAAAAAAAGRhdGEKACAAAAAAAAEAGABQFEPM6unYAVAUQ8zq6dgBUBRDzOrp2AFQSwUGAAAAAAEAAQBWAAAAsQAAAAAA" compressedBinaryValue="true" />
          <headers value="HTTP/1.1 200 OK&#xA;Content-Length: 120&#xD;&#xA;Server: nginx&#xD;&#xA;X-Frame-Options: DENY&#xD;&#xA;X-Content-Type-Options: nosniff&#xD;&#xA;Expires: 0&#xD;&#xA;X-XSS-Protection: 1; mode=block&#xD;&#xA;Connection: keep-alive&#xD;&#xA;Vary: Origin&#xD;&#xA;Vary: Access-Control-Request-Method&#xD;&#xA;Vary: Access-Control-Request-Headers&#xD;&#xA;Date: Thu, 27 Oct 2022 09:59:21 GMT&#xD;&#xA;Content-Type: application/json&#xD;&#xA;Pragma: no-cache&#xD;&#xA;Cache-Control: no-cache, no-store, max-age=0, must-revalidate&#xD;&#xA;" />
        </response>
        <sessionCookies />
      </request>
      <request scheme="http" host="192.168.13.159" path="/sys/system/page/list/save" port="20086" method="POST" RequestEncoding="65001" IsBodyEngineFiltered="False" IsWebSocket="False" SessionRequestType="Regular" ordinal="367" ValidationStatus="None" MultiStepTested="true" sequencePlaybackRequired="true">
        <raw encoding="none">POST /sys/system/page/list/save HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Referer: http://192.168.13.159:20086/udaam-ui/login?redirect=%2Fhome
Connection: keep-alive
Host: 192.168.13.159:20086
Content-Length: 44
Accept: application/json, text/plain, */*
Origin: http://192.168.13.159:20086
Authorization: Bearer 4fb2609d-004d-467c-bff8-7079e19ba830
Accept-Language: en-US
Content-Type: application/json;charset=UTF-8

{"loginType":"1","accountName":"superAdmin"}</raw>
        <parameter name="-&gt;&quot;loginType&quot;" captureIndex="-1" value="1" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="-&gt;&quot;loginType&quot;" />
        <parameter name="-&gt;&quot;accountName&quot;" captureIndex="-1" value="superAdmin" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="-&gt;&quot;accountName&quot;" />
        <response status="200" bodyEncoding="utf-8">
          <body value="UEsDBBQAAAAIAG2PW1VlUlO7awAAAHgAAAAEACQAZGF0YQoAIAAAAAAAAQAYAA4mRMzq6dgBDiZEzOrp2AEOJkTM6unYAS2KOw7CMAxAr4I8t5JtnIbkNsZuEUMFUsKE2CsmbsDp4Bx4YHyfO9jFZ6iMOEDr2m/tD+vcmp4iwXd7fZ5vGKCfQ3ZdryEZmUfCkfOOck2lMsXh2jXiQcox7U1ECjpPnrItTmlyUyskCzx+UEsBAi0AFAAAAAgAbY9bVWVSU7trAAAAeAAAAAQAJAAAAAAAAAAAAAAAAAAAAGRhdGEKACAAAAAAAAEAGAAOJkTM6unYAQ4mRMzq6dgBDiZEzOrp2AFQSwUGAAAAAAEAAQBWAAAAsQAAAAAA" compressedBinaryValue="true" />
          <headers value="HTTP/1.1 200 OK&#xA;Content-Length: 120&#xD;&#xA;Server: nginx&#xD;&#xA;X-Frame-Options: DENY&#xD;&#xA;X-Content-Type-Options: nosniff&#xD;&#xA;Expires: 0&#xD;&#xA;X-XSS-Protection: 1; mode=block&#xD;&#xA;Connection: keep-alive&#xD;&#xA;Vary: Origin&#xD;&#xA;Vary: Access-Control-Request-Method&#xD;&#xA;Vary: Access-Control-Request-Headers&#xD;&#xA;Date: Thu, 27 Oct 2022 09:59:21 GMT&#xD;&#xA;Content-Type: application/json&#xD;&#xA;Pragma: no-cache&#xD;&#xA;Cache-Control: no-cache, no-store, max-age=0, must-revalidate&#xD;&#xA;" />
        </response>
        <sessionCookies />
      </request>
      <request scheme="http" host="192.168.13.159" path="/sys/auth/info" port="20086" method="GET" RequestEncoding="28591" IsBodyEngineFiltered="False" IsWebSocket="False" SessionRequestType="Regular" ordinal="368" ValidationStatus="None" MultiStepTested="true" sequencePlaybackRequired="true">
        <raw encoding="none">GET /sys/auth/info HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Referer: http://192.168.13.159:20086/udaam-ui/login?redirect=%2Fhome
Connection: keep-alive
Host: 192.168.13.159:20086
Content-Length: 0
Accept: application/json, text/plain, */*
Authorization: Bearer 4fb2609d-004d-467c-bff8-7079e19ba830
Accept-Language: en-US

</raw>
        <response status="200" bodyEncoding="utf-8">
          <body value="UEsDBBQAAAAIAG2PW1XUIi4mKwEAABECAAAEACQAZGF0YQoAIAAAAAAAAQAYAPVLRMzq6dgB9UtEzOrp2AH1S0TM6unYAW1Ry0oDQRD8FZlzApsFCe4t5LQgEnxdxEM700mazGOZ6THGkLt48g/8Ov0O27jZJcHbVHVXd1fNVulgUFVlUQxUYuCcWuAwJVhISX2/fXy9f6qBYhKSwTVClkVZDkfFsByfjcbV+UVVjqTDAIOqtgq0DtlzbaSzED4njEfAg/sdnXKDcWIceeE96dXVP3wDKa1DFLnP1g4UmSn0KOHL4dksg8cDQAdkO+DhyWKnsUGv0Ny0dlvx2tyDJUO8UZX4h2fxEg/VEBd1v3KTGF2PpTjx5jpYrP08XFLibhGwJHbXSC44W5tbct19e4u1Qc80Jw1MwauKY0YJIkQ3OzFtEHjZg4Q+EdNrq5uDTSJMIUeN/WEN+en+e/+gjjIEj66AzMsQZRJKEA+Pu90PUEsBAi0AFAAAAAgAbY9bVdQiLiYrAQAAEQIAAAQAJAAAAAAAAAAAAAAAAAAAAGRhdGEKACAAAAAAAAEAGAD1S0TM6unYAfVLRMzq6dgB9UtEzOrp2AFQSwUGAAAAAAEAAQBWAAAAcQEAAAAA" compressedBinaryValue="true" />
          <headers value="HTTP/1.1 200 OK&#xA;Content-Length: 529&#xD;&#xA;Server: nginx&#xD;&#xA;X-Frame-Options: DENY&#xD;&#xA;X-Content-Type-Options: nosniff&#xD;&#xA;Expires: 0&#xD;&#xA;X-XSS-Protection: 1; mode=block&#xD;&#xA;Connection: keep-alive&#xD;&#xA;Vary: Origin&#xD;&#xA;Vary: Access-Control-Request-Method&#xD;&#xA;Vary: Access-Control-Request-Headers&#xD;&#xA;Date: Thu, 27 Oct 2022 09:59:21 GMT&#xD;&#xA;Content-Type: application/json&#xD;&#xA;Pragma: no-cache&#xD;&#xA;Cache-Control: no-cache, no-store, max-age=0, must-revalidate&#xD;&#xA;" />
        </response>
        <sessionCookies />
      </request>
      <request scheme="http" host="192.168.13.159" path="/sys/sysresourcesconfig/list" port="20086" method="GET" RequestEncoding="28591" IsBodyEngineFiltered="False" IsWebSocket="False" SessionRequestType="Regular" ordinal="369" ValidationStatus="None" MultiStepTested="true" sequencePlaybackRequired="true">
        <raw encoding="none">GET /sys/sysresourcesconfig/list?pageSize=9999 HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Referer: http://192.168.13.159:20086/udaam-ui/login?redirect=%2Fhome
Connection: keep-alive
Host: 192.168.13.159:20086
Content-Length: 0
Accept: application/json, text/plain, */*
Authorization: Bearer 4fb2609d-004d-467c-bff8-7079e19ba830
Accept-Language: en-US

</raw>
        <parameter name="pageSize" captureIndex="0" value="9999" type="QUERY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="pageSize" />
        <response status="200" bodyEncoding="utf-8">
          <body value="UEsDBBQAAAAIAG2PW1VXV3jcLwQAAAoSAAAEACQAZGF0YQoAIAAAAAAAAQAYAPVLRMzq6dgB9UtEzOrp2AH1S0TM6unYAdWYS28bVRTHvwqadRLd98N7FmxYwQqxuM8mku0Ye8KCKFKq1k1UJU1Qm6YgRAhtaKQofQhQqF2pXyYz03wLjnGR74RaglUHe+N7PHc8v3P/53/P9XrmVn3IWgShhWyQm3xt8G7QCYOBuQFfZeX2fnH3KFvI8hUI5qbTgyBBhCxitEjkR1i2uG4RDFd4k5ustQ437eahm2etL9azFQ+Xe0WNRxIhxzXBlgchNKIkYk1sjDzC3OmDZGt+OfRg2DWdybC4eVIefFc8uV0+fAXR3mo/n/w6pQRGy6uD/NPpdTAKXWPb8DnvrwW4XT+YPHy2Mvm2u9Zu/x35fBD6n/h/xqb3mUbXev7a3GmkPncWm83dWHgHHKUz3hodJXVWRG5UxICPlNbUWO1S4P7ySkp8fnA5elr8sjXDxZg0HFdJqYNyhlMauVdcEKGoxTZESw1XZIbr7KAzgy03x9XoTUJK6FzQaNqDD0/qDDEKaR01w9wxQZG0wnJEmRbUqkTJHZ+AXv4xLg9elLvP/k+skQXOg6OR8sB9jMizaJlwUMHeWlSrWmfDcr9Wt8Xoojx+XB5vF7t7xf7ODBxSplQdHXxgCQu1hOkSVrpxicCQBkMYPDeVyIngo9VEEWZsBGOjrp4Ily58Ofy5OhxOU1A9O67271S/jqvx0SwdoCbUcCEQogx2HjunuRdRGEsV95piZkHy3qT8/sZXKf5fon/72+nV1l6KTMX7BQBv2TRz40hQZZkkHhycU4aIMdwyRSPjyEWUmJtPS+DJ99X4fvnj7Wn0X1R9I2gpLKmMngliJONYSx4th9qP0TuOKa/Rdmq45Q+jKW6nxsuaDWylk5IiY6hyAUfksMCYwR4GtR2lIKm4QydZ4OrB78X5/qS67915++LW1aNhMXx5OTq7XuCCwqvZOYCCRMLiKLl3MkRGtJEetjotLWFM13LgOoNk1XfG1cPDq8Pz6t7zOfZGrpt94+xNQA+KjbZWx6iCNoS4qKwAZ9OWuUATyS/3apJ/evVqrxq/BvK0W0Oo4e2acIFFypwCmcM2hqE390SqIC2b7Gw1P18ZpM3pzqg4Oip2z6oHR8Bd7G+ni75Y7myVP20VFyfF8CJRANa42fnwIlguBAnRaUV8ALPnJCrFIpSBSR3+G5vb/5qO47Py7kktHfMLohHpkEgGpqLzSjlOjXHaB8G5AE8MnuH64cW9Rx6TZufq8LTcvkhdUKGGy8DA8SwSKR2YIGz0JEjuEJxiFGx+irmaC/ZWU+7hafHto8vRqNh7fPnmuLz5vBjdTxxBESwb7oGEBzjQhMg149DYIqokHNCDNQEUAIfWeouXot+a9njzmlslGr7oHptgnHKURKNYiJP/KSQ0vNo4bkMN3H2dgO++LDdPis3Xc7v6+Uv+QcG/XMjy1dy0P26HTujmg6yF1cbGn1BLAQItABQAAAAIAG2PW1VXV3jcLwQAAAoSAAAEACQAAAAAAAAAAAAAAAAAAABkYXRhCgAgAAAAAAABABgA9UtEzOrp2AH1S0TM6unYAfVLRMzq6dgBUEsFBgAAAAABAAEAVgAAAHUEAAAAAA==" compressedBinaryValue="true" />
          <headers value="HTTP/1.1 200 OK&#xA;Content-Length: 4618&#xD;&#xA;Server: nginx&#xD;&#xA;X-Frame-Options: DENY&#xD;&#xA;X-Content-Type-Options: nosniff&#xD;&#xA;Expires: 0&#xD;&#xA;X-XSS-Protection: 1; mode=block&#xD;&#xA;Connection: keep-alive&#xD;&#xA;Vary: Origin&#xD;&#xA;Vary: Access-Control-Request-Method&#xD;&#xA;Vary: Access-Control-Request-Headers&#xD;&#xA;Date: Thu, 27 Oct 2022 09:59:21 GMT&#xD;&#xA;Content-Type: application/json&#xD;&#xA;Pragma: no-cache&#xD;&#xA;Cache-Control: no-cache, no-store, max-age=0, must-revalidate&#xD;&#xA;" />
        </response>
        <sessionCookies />
      </request>
    </RecordedSessionRequests>
    <SessionVerifier>
      <Enable>True</Enable>
      <OutSession>False</OutSession>
      <Pattern Base64="False">200\s+OK</Pattern>
      <PatternType>RegularExpression</PatternType>
      <request scheme="http" host="192.168.13.159" path="/sys/system/page/list/save" port="20086" method="POST" RequestEncoding="65001" IsBodyEngineFiltered="False" IsWebSocket="False" SessionRequestType="Regular" ordinal="367" ValidationStatus="None" MultiStepTested="true" sequencePlaybackRequired="true">
        <raw encoding="none">POST /sys/system/page/list/save HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Referer: http://192.168.13.159:20086/udaam-ui/login?redirect=%2Fhome
Connection: keep-alive
Host: 192.168.13.159:20086
Content-Length: 44
Accept: application/json, text/plain, */*
Origin: http://192.168.13.159:20086
Authorization: Bearer 4fb2609d-004d-467c-bff8-7079e19ba830
Accept-Language: en-US
Content-Type: application/json;charset=UTF-8

{"loginType":"1","accountName":"superAdmin"}</raw>
        <parameter name="-&gt;&quot;loginType&quot;" captureIndex="-1" value="1" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="-&gt;&quot;loginType&quot;" />
        <parameter name="-&gt;&quot;accountName&quot;" captureIndex="-1" value="superAdmin" type="BODY" linkParamType="simplelink" separator="&amp;" operator="=" reportName="-&gt;&quot;accountName&quot;" />
        <response status="200" bodyEncoding="utf-8">
          <body value="UEsDBBQAAAAIAG2PW1VlUlO7awAAAHgAAAAEACQAZGF0YQoAIAAAAAAAAQAYAA4mRMzq6dgBDiZEzOrp2AEOJkTM6unYAS2KOw7CMAxAr4I8t5JtnIbkNsZuEUMFUsKE2CsmbsDp4Bx4YHyfO9jFZ6iMOEDr2m/tD+vcmp4iwXd7fZ5vGKCfQ3ZdryEZmUfCkfOOck2lMsXh2jXiQcox7U1ECjpPnrItTmlyUyskCzx+UEsBAi0AFAAAAAgAbY9bVWVSU7trAAAAeAAAAAQAJAAAAAAAAAAAAAAAAAAAAGRhdGEKACAAAAAAAAEAGAAOJkTM6unYAQ4mRMzq6dgBDiZEzOrp2AFQSwUGAAAAAAEAAQBWAAAAsQAAAAAA" compressedBinaryValue="true" />
          <headers value="HTTP/1.1 200 OK&#xA;Content-Length: 120&#xD;&#xA;Server: nginx&#xD;&#xA;X-Frame-Options: DENY&#xD;&#xA;X-Content-Type-Options: nosniff&#xD;&#xA;Expires: 0&#xD;&#xA;X-XSS-Protection: 1; mode=block&#xD;&#xA;Connection: keep-alive&#xD;&#xA;Vary: Origin&#xD;&#xA;Vary: Access-Control-Request-Method&#xD;&#xA;Vary: Access-Control-Request-Headers&#xD;&#xA;Date: Thu, 27 Oct 2022 09:59:21 GMT&#xD;&#xA;Content-Type: application/json&#xD;&#xA;Pragma: no-cache&#xD;&#xA;Cache-Control: no-cache, no-store, max-age=0, must-revalidate&#xD;&#xA;" />
        </response>
        <sessionCookies />
      </request>
    </SessionVerifier>
    <InSessionRequestIndex>4</InSessionRequestIndex>
    <ActionBasedSequence RecordingBrowser="Chromium">
      <Enabled>True</Enabled>
      <UseAbl>True</UseAbl>
      <StartingUrl>http://192.168.13.159:20086/udaam-ui</StartingUrl>
      <Actions>
        <Action ActionType="Wait" BrowserIndex="0" Validated="Success" ID="c6100015-1024-46c9-a6e8-a4faff49ea67">
          <ElementLocations>
            <ElementLocation isPreferred="False">
              <tagName name="A" />
              <attributes>
                <attribute key="NAME" value="wait(sec)" />
              </attributes>
            </ElementLocation>
          </ElementLocations>
          <Value>0</Value>
          <ProxyOrdinalRequestBeforeAction>-1</ProxyOrdinalRequestBeforeAction>
        </Action>
        <Action ActionType="Click" BrowserIndex="0" Validated="Success" ID="6118bfc4-0c40-4f68-8c17-3c177c0843df">
          <ElementLocations>
            <ElementLocation isPreferred="False">
              <hybridXPath>//*[@id='pane-passwordLogin']/FORM[1]/DIV[1]/DIV[1]/DIV[1]/INPUT[1]</hybridXPath>
              <xPath>//HTML[1]/BODY[1]/DIV[1]/DIV[2]/DIV[2]/DIV[1]/DIV[2]/DIV[2]/DIV[2]/DIV[1]/FORM[1]/DIV[1]/DIV[1]/DIV[1]/INPUT[1]</xPath>
              <tagName name="INPUT" />
              <parentForm>&lt;FORM  data-v-b5967b8a="" class="el-form form" /&gt;</parentForm>
              <attributes>
                <attribute key="type" value="text" />
                <attribute key="autocomplete" value="off" />
                <attribute key="placeholder" value="请输入账号" />
                <attribute key="class" value="el-input__inner" />
              </attributes>
            </ElementLocation>
          </ElementLocations>
          <ProxyOrdinalRequestBeforeAction>-1</ProxyOrdinalRequestBeforeAction>
        </Action>
        <Action ActionType="Set" BrowserIndex="0" Validated="Success" ID="2bd05af8-e979-4e28-9bdc-48b754eba6a3">
          <ElementLocations>
            <ElementLocation isPreferred="False">
              <hybridXPath>//*[@id='pane-passwordLogin']/FORM[1]/DIV[1]/DIV[1]/DIV[1]/INPUT[1]</hybridXPath>
              <xPath>//HTML[1]/BODY[1]/DIV[1]/DIV[2]/DIV[2]/DIV[1]/DIV[2]/DIV[2]/DIV[2]/DIV[1]/FORM[1]/DIV[1]/DIV[1]/DIV[1]/INPUT[1]</xPath>
              <tagName name="INPUT" />
              <parentForm>&lt;FORM  data-v-b5967b8a="" class="el-form form" /&gt;</parentForm>
              <attributes>
                <attribute key="type" value="text" />
                <attribute key="autocomplete" value="off" />
                <attribute key="placeholder" value="请输入账号" />
                <attribute key="class" value="el-input__inner" />
                <attribute key="value" value="s" />
              </attributes>
            </ElementLocation>
          </ElementLocations>
          <Value Base64="true" Encrypted="true">YXN2DNOCcrqgXANgNP3JVUNHsVFIZdNMeon1J9iKnZs=</Value>
          <ProxyOrdinalRequestBeforeAction>-1</ProxyOrdinalRequestBeforeAction>
        </Action>
        <Action ActionType="Set" BrowserIndex="0" Validated="Success" ID="9b9b23be-7e02-4af7-b032-13b620925c36">
          <ElementLocations>
            <ElementLocation isPreferred="False">
              <hybridXPath>//*[@id='pane-passwordLogin']/FORM[1]/DIV[2]/DIV[1]/DIV[1]/INPUT[1]</hybridXPath>
              <xPath>//HTML[1]/BODY[1]/DIV[1]/DIV[2]/DIV[2]/DIV[1]/DIV[2]/DIV[2]/DIV[2]/DIV[1]/FORM[1]/DIV[2]/DIV[1]/DIV[1]/INPUT[1]</xPath>
              <tagName name="INPUT" />
              <parentForm>&lt;FORM  data-v-b5967b8a="" class="el-form form" /&gt;</parentForm>
              <attributes>
                <attribute key="type" value="password" />
                <attribute key="autocomplete" value="off" />
                <attribute key="placeholder" value="请输入密码" />
                <attribute key="class" value="el-input__inner" />
                <attribute key="value" value="s" />
              </attributes>
            </ElementLocation>
          </ElementLocations>
          <Value Base64="true" Encrypted="true">YXN2DNOCcrqgXANgNP3JVUNHsVFIZdNMeon1J9iKnZs=</Value>
          <ProxyOrdinalRequestBeforeAction>-1</ProxyOrdinalRequestBeforeAction>
        </Action>
        <Action ActionType="Set" BrowserIndex="0" Validated="Success" ID="50cd1941-6700-4af4-9dcf-0ecc04100781">
          <ElementLocations>
            <ElementLocation isPreferred="False">
              <hybridXPath>//*[@id='pane-passwordLogin']/FORM[1]/DIV[3]/DIV[1]/DIV[1]/INPUT[1]</hybridXPath>
              <xPath>//HTML[1]/BODY[1]/DIV[1]/DIV[2]/DIV[2]/DIV[1]/DIV[2]/DIV[2]/DIV[2]/DIV[1]/FORM[1]/DIV[3]/DIV[1]/DIV[1]/INPUT[1]</xPath>
              <tagName name="INPUT" />
              <parentForm>&lt;FORM  data-v-b5967b8a="" class="el-form form" /&gt;</parentForm>
              <attributes>
                <attribute key="type" value="text" />
                <attribute key="autocomplete" value="off" />
                <attribute key="placeholder" value="请输入验证码" />
                <attribute key="class" value="el-input__inner" />
                <attribute key="value" value="5" />
              </attributes>
            </ElementLocation>
          </ElementLocations>
          <Value Base64="true" Encrypted="true">0X800D23Tdrcrevx3PibSA==</Value>
          <ProxyOrdinalRequestBeforeAction>-1</ProxyOrdinalRequestBeforeAction>
        </Action>
        <Action ActionType="Wait" BrowserIndex="0" Validated="Success" ID="c29263a2-346a-4b97-872d-fcf3070021e1">
          <ElementLocations>
            <ElementLocation isPreferred="False">
              <tagName name="A" />
              <attributes>
                <attribute key="NAME" value="wait(sec)" />
              </attributes>
            </ElementLocation>
          </ElementLocations>
          <Value>0</Value>
          <ProxyOrdinalRequestBeforeAction>-1</ProxyOrdinalRequestBeforeAction>
        </Action>
        <Action ActionType="Click" BrowserIndex="0" Validated="Success" ID="41219758-0fe5-46dc-a903-352395b0e062">
          <ElementLocations>
            <ElementLocation isPreferred="False">
              <hybridXPath>//*[@id='pane-passwordLogin']/FORM[1]/DIV[4]/DIV[1]/BUTTON[1]/SPAN[1]</hybridXPath>
              <xPath>//HTML[1]/BODY[1]/DIV[1]/DIV[2]/DIV[2]/DIV[1]/DIV[2]/DIV[2]/DIV[2]/DIV[1]/FORM[1]/DIV[4]/DIV[1]/BUTTON[1]/SPAN[1]</xPath>
              <tagName name="SPAN" />
              <innerText>登 录</innerText>
              <parentForm>&lt;FORM  data-v-b5967b8a="" class="el-form form" /&gt;</parentForm>
            </ElementLocation>
          </ElementLocations>
          <ProxyOrdinalRequestBeforeAction>-1</ProxyOrdinalRequestBeforeAction>
        </Action>
        <Action ActionType="Wait" BrowserIndex="0" Validated="Success" ID="cb6c2679-df92-4aaf-96b9-aaa7b5b8bf3f">
          <ElementLocations>
            <ElementLocation isPreferred="False">
              <tagName name="A" />
              <attributes>
                <attribute key="NAME" value="wait(sec)" />
              </attributes>
            </ElementLocation>
          </ElementLocations>
          <Value>3</Value>
          <ProxyOrdinalRequestBeforeAction>-1</ProxyOrdinalRequestBeforeAction>
        </Action>
      </Actions>
      <VerifyElementsActionThreshold>0.6</VerifyElementsActionThreshold>
      <LogoutRegex>log[_\-\s]?out|sign[_\-\s]?out|log[_\-\s]?off|sign[_\-\s]?off|exit|quit|bye-bye|clearuser|invalidate|sign out|sign off|log out|log off|disconnect</LogoutRegex>
    </ActionBasedSequence>
    <VariablesDefinitions>
      <VariableDefinition IsRegularExpression="False" Name="">
        <VariableType>DefaultDefinitions</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>None</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="^BV_">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="^CFID">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="^CFTOKEN">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__VIEWSTATE">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__EVENTVALIDATION">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__REQUESTDIGEST">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__VIEWSTATEGENERATOR">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__EVENTARGUMENT">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>None</RequestIgnoreStatus>
        <EntityIgnoreStatus>None</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__EVENTTARGET">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>None</RequestIgnoreStatus>
        <EntityIgnoreStatus>None</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__VIEWSTATEID">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path>/</Path>
        <Comments>An id of the viewstate that is stored in the server's db. </Comments>
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__LASTFOCUS">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path>/</Path>
        <Comments />
        <RequestIgnoreStatus>Full</RequestIgnoreStatus>
        <EntityIgnoreStatus>Full</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__SCROLLPOSITIONX">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path>/</Path>
        <Comments />
        <RequestIgnoreStatus>Full</RequestIgnoreStatus>
        <EntityIgnoreStatus>Full</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__SCROLLPOSITIONY">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path>/</Path>
        <Comments />
        <RequestIgnoreStatus>Full</RequestIgnoreStatus>
        <EntityIgnoreStatus>Full</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__PREVIOUSPAGE">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path>/</Path>
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__CALLBACKID">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path>/</Path>
        <Comments />
        <RequestIgnoreStatus>None</RequestIgnoreStatus>
        <EntityIgnoreStatus>None</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__CALLBACKPARAM">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path>/</Path>
        <Comments />
        <RequestIgnoreStatus>None</RequestIgnoreStatus>
        <EntityIgnoreStatus>None</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="__VIEWSTATEFIELDCOUNT">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path>/</Path>
        <Comments />
        <RequestIgnoreStatus>Full</RequestIgnoreStatus>
        <EntityIgnoreStatus>Full</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="__VIEWSTATE\d+">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path>/</Path>
        <Comments />
        <RequestIgnoreStatus>Full</RequestIgnoreStatus>
        <EntityIgnoreStatus>Full</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="wsdl">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Full</RequestIgnoreStatus>
        <EntityIgnoreStatus>Full</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="disco">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Full</RequestIgnoreStatus>
        <EntityIgnoreStatus>Full</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="javax.faces.viewstate">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="^BV_">
        <VariableType>Cookie</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="JSESSIONID">
        <VariableType>Custom</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="IIS_COOKIELESS">
        <VariableType>Custom</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="ses|token">
        <VariableType>Cookie</VariableType>
        <Hosts />
        <Path />
        <Comments>Session cookie regular expression</Comments>
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="(?:server|user|u)_*id">
        <VariableType>Cookie</VariableType>
        <Hosts />
        <Path />
        <Comments>Server or user id</Comments>
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="JSESSIONID">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="PHPSESSID">
        <VariableType>Parameter</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="__utm.|vgnvisitor|_csuid|_csoot|WEBTRENDS_ID|WT_FPS|cookieenabledcheck|__qc[ab]|MintUnique|PD_STATEFUL|_sn|BCSI\\-">
        <VariableType>Cookie</VariableType>
        <Hosts />
        <Path />
        <Comments>Cookie that tracks visitor activity for a third-party application</Comments>
        <RequestIgnoreStatus>Full</RequestIgnoreStatus>
        <EntityIgnoreStatus>Full</EntityIgnoreStatus>
        <ExcludeFromTest>True</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="(ASPSESSIONID[a-zA-Z0-9]{8})">
        <VariableType>Cookie</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>None</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>True</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="WC_AUTHENTICATION_(\d+)">
        <VariableType>Cookie</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>None</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>True</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="True" Name="WC_USERACTIVITY_(\d+)">
        <VariableType>Cookie</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>None</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>True</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="GUID">
        <VariableType>Custom</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="NUMERIC">
        <VariableType>Custom</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="HEXDECIMAL">
        <VariableType>Custom</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="DATE">
        <VariableType>Custom</VariableType>
        <Hosts />
        <Path />
        <Comments />
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>False</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>-1</CaptureIndex>
        <VariableOrigin>TemplateDefined</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="password">
        <VariableType>Parameter</VariableType>
        <Hosts>192.168.13.159</Hosts>
        <Path />
        <Comments>从手动登录顺序记录抽取</Comments>
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>0</CaptureIndex>
        <VariableOrigin>Login</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="secret">
        <VariableType>Parameter</VariableType>
        <Hosts>192.168.13.159</Hosts>
        <Path />
        <Comments>从手动登录顺序记录抽取</Comments>
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>0</CaptureIndex>
        <VariableOrigin>Login</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
      <VariableDefinition IsRegularExpression="False" Name="key">
        <VariableType>Parameter</VariableType>
        <Hosts>192.168.13.159</Hosts>
        <Path />
        <Comments>从手动登录顺序记录抽取</Comments>
        <RequestIgnoreStatus>Value</RequestIgnoreStatus>
        <EntityIgnoreStatus>Value</EntityIgnoreStatus>
        <ExcludeFromTest>False</ExcludeFromTest>
        <SessionIDEnabled>True</SessionIDEnabled>
        <CaptureName />
        <CaptureIndex>0</CaptureIndex>
        <VariableOrigin>Login</VariableOrigin>
        <AlwaysSend>False</AlwaysSend>
        <IsGroup>False</IsGroup>
        <SessionID TrackingMethod="ExploreAndLogin">
          <Value />
        </SessionID>
      </VariableDefinition>
    </VariablesDefinitions>
    <CustomParameters>
      <CustomParameter LogicalName="JSESSIONID">
        <Pattern>;(?:JSESSIONID|jsessionid)=([^/]+)$</Pattern>
        <NameGroupIndex>-1</NameGroupIndex>
        <ValueGroupIndex>1</ValueGroupIndex>
        <TargetSegment>Path</TargetSegment>
        <ResponsePattern />
        <Condition />
      </CustomParameter>
      <CustomParameter LogicalName="IIS_COOKIELESS">
        <Pattern>(\((?:[ASF]\([a-zA-Z0-9]+\)){1,3}\))</Pattern>
        <NameGroupIndex>-1</NameGroupIndex>
        <ValueGroupIndex>1</ValueGroupIndex>
        <TargetSegment>Path</TargetSegment>
        <ResponsePattern />
        <Condition />
      </CustomParameter>
      <CustomParameter LogicalName="GUID">
        <Pattern>((\{){0,1}[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}(\}){0,1})</Pattern>
        <NameGroupIndex>-1</NameGroupIndex>
        <ValueGroupIndex>1</ValueGroupIndex>
        <TargetSegment>Path</TargetSegment>
        <ResponsePattern />
        <Condition />
      </CustomParameter>
      <CustomParameter LogicalName="HEXDECIMAL">
        <Pattern>(([A-Fa-f0-9]{40})|([A-Fa-f0-9]{32}))</Pattern>
        <NameGroupIndex>-1</NameGroupIndex>
        <ValueGroupIndex>1</ValueGroupIndex>
        <TargetSegment>Path</TargetSegment>
        <ResponsePattern />
        <Condition />
      </CustomParameter>
      <CustomParameter LogicalName="DATE">
        <Pattern>\b((19|20)\d\d[-/.](0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01]))\b</Pattern>
        <NameGroupIndex>-1</NameGroupIndex>
        <ValueGroupIndex>1</ValueGroupIndex>
        <TargetSegment>Path</TargetSegment>
        <ResponsePattern />
        <Condition />
      </CustomParameter>
      <CustomParameter LogicalName="NUMERIC">
        <Pattern>\b(\d{8,128})\b</Pattern>
        <NameGroupIndex>-1</NameGroupIndex>
        <ValueGroupIndex>1</ValueGroupIndex>
        <TargetSegment>Path</TargetSegment>
        <ResponsePattern />
        <Condition />
      </CustomParameter>
    </CustomParameters>
  </SessionManagement>
  <customHeaders>
    <customHeader>
      <Name>Authorization</Name>
      <HeaderValue>Bearer {0}</HeaderValue>
      <ExtractValueFromBodyRegEx>(?i)["|']access_token["|']\s*[:|=]\s*["|']([A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12})["|']</ExtractValueFromBodyRegEx>
      <Enabled>True</Enabled>
      <Type>2</Type>
    </customHeader>
  </customHeaders>
  <UserInput>
    <FormFiller Version="2.0" Enabled="True" DefaultValue="1234" UseDefaultValue="True" RandomDefaultValue="False">
      <Group LogicalName="InternalAppScanUserName" MatchType="Partial" Action="">
        <Name>InternalAppScanUserName</Name>
        <Selection>Ignore</Selection>
        <Value>5264</Value>
        <MatchNames>
          <MatchName>code</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="InternalAppScanPassword" MatchType="Partial" Action="">
        <Name>InternalAppScanPassword</Name>
        <Selection>Ignore</Selection>
        <Value Encrypt="true">9UFxrhTwnMSkbzjIGZGPJQ==</Value>
        <MatchNames>
          <MatchName>username</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Address" MatchType="Partial" Action="">
        <Name>地址</Name>
        <Selection>Ignore</Selection>
        <Value>753 Main Street</Value>
        <MatchNames>
          <MatchName>地址</MatchName>
          <MatchName>addr</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Age" MatchType="Partial" Action="">
        <Name>年龄</Name>
        <Selection>Ignore</Selection>
        <Value>25</Value>
        <MatchNames>
          <MatchName>年龄</MatchName>
          <MatchName>age</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Areacode" MatchType="Partial" Action="">
        <Name>区号</Name>
        <Selection>Ignore</Selection>
        <Value>555</Value>
        <MatchNames>
          <MatchName>区域</MatchName>
          <MatchName>area</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="City" MatchType="Partial" Action="">
        <Name>城市</Name>
        <Selection>Ignore</Selection>
        <Value>Mystery</Value>
        <MatchNames>
          <MatchName>城市</MatchName>
          <MatchName>city</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Company" MatchType="Partial" Action="">
        <Name>公司</Name>
        <Selection>Ignore</Selection>
        <Value>Acme-Hackme Corp.</Value>
        <MatchNames>
          <MatchName>公司</MatchName>
          <MatchName>公司</MatchName>
          <MatchName>company</MatchName>
          <MatchName>firm</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Country" MatchType="Partial" Action="">
        <Name>国家或地区</Name>
        <Selection>Ignore</Selection>
        <Value>USA</Value>
        <MatchNames>
          <MatchName>国家或地区</MatchName>
          <MatchName>country</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Email" MatchType="Partial" Action="">
        <Name>电子邮件</Name>
        <Selection>Ignore</Selection>
        <Value>test@altoromutual.com</Value>
        <MatchNames>
          <MatchName>邮件</MatchName>
          <MatchName>mail</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="MailTo" MatchType="Complete" Action="">
        <Name>收件人</Name>
        <Selection>Ignore</Selection>
        <Value>test@altoromutual.com</Value>
        <MatchNames>
          <MatchName>收件人</MatchName>
          <MatchName>收件人</MatchName>
          <MatchName>To</MatchName>
          <MatchName>to</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="MailFrom" MatchType="Complete" Action="">
        <Name>发件人</Name>
        <Selection>Ignore</Selection>
        <Value>test@altoromutual.com</Value>
        <MatchNames>
          <MatchName>发件人</MatchName>
          <MatchName>发件人</MatchName>
          <MatchName>From</MatchName>
          <MatchName>from</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="MailBcc" MatchType="Complete" Action="">
        <Name>邮件密送</Name>
        <Selection>Ignore</Selection>
        <Value>test@altoromutual.com</Value>
        <MatchNames>
          <MatchName>密件抄送</MatchName>
          <MatchName>密件抄送</MatchName>
          <MatchName>Bcc</MatchName>
          <MatchName>bcc</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Day" MatchType="Partial" Action="">
        <Name>天</Name>
        <Selection>Ignore</Selection>
        <Value>01</Value>
        <MatchNames>
          <MatchName>天</MatchName>
          <MatchName>day</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Month" MatchType="Partial" Action="">
        <Name>月</Name>
        <Selection>Ignore</Selection>
        <Value>01</Value>
        <MatchNames>
          <MatchName>月</MatchName>
          <MatchName>month</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Number" MatchType="Partial" Action="">
        <Name>号码</Name>
        <Selection>Ignore</Selection>
        <Value>9876543210</Value>
        <MatchNames>
          <MatchName>号码</MatchName>
          <MatchName>num</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Passport" MatchType="Complete" Action="">
        <Name>护照</Name>
        <Selection>Ignore</Selection>
        <Value>9876543210</Value>
        <MatchNames>
          <MatchName>护照</MatchName>
          <MatchName>护照</MatchName>
          <MatchName>护照</MatchName>
          <MatchName>passport</MatchName>
          <MatchName>Passport</MatchName>
          <MatchName>PASSPORT</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Phone" MatchType="Partial" Action="">
        <Name>电话</Name>
        <Selection>Ignore</Selection>
        <Value>555-555-5555</Value>
        <MatchNames>
          <MatchName>电话</MatchName>
          <MatchName>电话</MatchName>
          <MatchName>tel</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="SocialSecurity" MatchType="Partial" Action="">
        <Name>社会保险</Name>
        <Selection>Ignore</Selection>
        <Value>987 65 4321</Value>
        <MatchNames>
          <MatchName>社会保险号码</MatchName>
          <MatchName>社会</MatchName>
          <MatchName>ssn</MatchName>
          <MatchName>social</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="State" MatchType="Partial" Action="">
        <Name>状态</Name>
        <Selection>Ignore</Selection>
        <Value>AK</Value>
        <MatchNames>
          <MatchName>州</MatchName>
          <MatchName>state</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Year" MatchType="Partial" Action="">
        <Name>年份</Name>
        <Selection>Ignore</Selection>
        <Value>09</Value>
        <MatchNames>
          <MatchName>年份</MatchName>
          <MatchName>year</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="ZipCode" MatchType="Partial" Action="">
        <Name>邮编</Name>
        <Selection>Ignore</Selection>
        <Value>99801</Value>
        <MatchNames>
          <MatchName>邮编</MatchName>
          <MatchName>邮编</MatchName>
          <MatchName>zip</MatchName>
          <MatchName>postal</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="Date" MatchType="Partial" Action="">
        <Name>日期</Name>
        <Selection>Ignore</Selection>
        <Value>2019-01-01</Value>
        <MatchNames>
          <MatchName>日期</MatchName>
          <MatchName>date</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/authorization/oauth/token">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>password</Value>
        <MatchNames>
          <MatchName>grant_type</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/authorization/oauth/token">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>YdJSh1yGAUzpToQdAsuGHTceOxtr+Vkb1JA5GXXsnGuueHnOxuipHWpEhEA1p2Ke3gvuePknUC77tBvdtHcZfg==</Value>
        <MatchNames>
          <MatchName>password</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/authorization/oauth/token">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>YdJSh1yGAUzpToQdAsuGHTceOxtr+Vkb1JA5GXXsnGuueHnOxuipHWpEhEA1p2Ke3gvuePknUC77tBvdtHcZfg==</Value>
        <MatchNames>
          <MatchName>secret</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/authorization/oauth/token">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>1666353336456</Value>
        <MatchNames>
          <MatchName>key</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/system/page/list/save">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>1</Value>
        <MatchNames>
          <MatchName>-&gt;"loginType"</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/system/page/list/save">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>superAdmin</Value>
        <MatchNames>
          <MatchName>-&gt;"accountName"</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/appInfo/list?supplierId=&amp;seachStr=&amp;systemId=&amp;typeId=&amp;enabled=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>supplierId</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/appInfo/list?supplierId=&amp;seachStr=&amp;systemId=&amp;typeId=&amp;enabled=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>typeId</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/threeAppInfo/list?insideFlag=false">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>false</Value>
        <MatchNames>
          <MatchName>insideFlag</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/menuManage/page/getPermissionList?seachStr=&amp;systemId=108d94546ccfa28fa2bf23a3c9701f4e&amp;pid=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>seachStr</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/menuManage/page/getPermissionList?seachStr=&amp;systemId=108d94546ccfa28fa2bf23a3c9701f4e&amp;pid=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>pid</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/applicationRole/page/findList?sysName=">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>sysName</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/applicationRole/page/findAllRoleBySystem?systemId=3c8a5cc207f6a82df3411330cb954569&amp;roleName=">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>roleName</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/account/page/findUserAccount?accountName=&amp;uName=&amp;idCard=&amp;phone=&amp;email=&amp;enabled=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>accountName</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/account/page/findUserAccount?accountName=&amp;uName=&amp;idCard=&amp;phone=&amp;email=&amp;enabled=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>idCard</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/account/page/findUserAccount?accountName=&amp;uName=&amp;idCard=&amp;phone=&amp;email=&amp;enabled=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>phone</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/account/page/findUserAccount?accountName=&amp;uName=&amp;idCard=&amp;phone=&amp;email=&amp;enabled=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>email</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/org/page/list?code=&amp;name=&amp;enabled=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>enabled</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/org/page/loadUserOrg?isTree=true">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>true</Value>
        <MatchNames>
          <MatchName>isTree</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/loginLog/list?uName=&amp;account=&amp;requestIp=&amp;startOpenTime=2022-10-15+00:00:00&amp;endOpenTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>account</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/loginLog/list?uName=&amp;account=&amp;requestIp=&amp;startOpenTime=2022-10-15+00:00:00&amp;endOpenTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>requestIp</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/orgReportForms/page/logTrend?orgId=07dad06e0445bb46ca6e0304d4302b76&amp;beginTime=2022-10-15&amp;endTime=2022-10-21&amp;systemId=&amp;type=1">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>1</Value>
        <MatchNames>
          <MatchName>type</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/orgReportForms/page/activeRanking?orgId=07dad06e0445bb46ca6e0304d4302b76&amp;beginTime=2022-10-15&amp;endTime=2022-10-21&amp;systemId=&amp;order=desc&amp;pageSize=10&amp;pageNum=1">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>desc</Value>
        <MatchNames>
          <MatchName>order</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/siteAccessLog/page/list?startOpenTime=2022-10-15+00:00:00&amp;endOpenTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>2022-10-15+00:00:00</Value>
        <MatchNames>
          <MatchName>startOpenTime</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/siteAccessLog/page/list?startOpenTime=2022-10-15+00:00:00&amp;endOpenTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>2022-10-21+23:59:59</Value>
        <MatchNames>
          <MatchName>endOpenTime</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/grantOperationLog/page/list?uName=&amp;orgId=&amp;beginDate=2022-10-15+00:00:00&amp;endDate=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>2022-10-15+00:00:00</Value>
        <MatchNames>
          <MatchName>beginDate</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/grantOperationLog/page/list?uName=&amp;orgId=&amp;beginDate=2022-10-15+00:00:00&amp;endDate=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>2022-10-21+23:59:59</Value>
        <MatchNames>
          <MatchName>endDate</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/log/page/list?status=&amp;uName=&amp;requestIP=&amp;orgId=&amp;systemId=&amp;apiName=&amp;beginTime=2022-10-15+00:00:00&amp;endTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>status</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/log/page/list?status=&amp;uName=&amp;requestIP=&amp;orgId=&amp;systemId=&amp;apiName=&amp;beginTime=2022-10-15+00:00:00&amp;endTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>uName</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/log/page/list?status=&amp;uName=&amp;requestIP=&amp;orgId=&amp;systemId=&amp;apiName=&amp;beginTime=2022-10-15+00:00:00&amp;endTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>requestIP</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/log/page/list?status=&amp;uName=&amp;requestIP=&amp;orgId=&amp;systemId=&amp;apiName=&amp;beginTime=2022-10-15+00:00:00&amp;endTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>orgId</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/log/page/list?status=&amp;uName=&amp;requestIP=&amp;orgId=&amp;systemId=&amp;apiName=&amp;beginTime=2022-10-15+00:00:00&amp;endTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>systemId</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/log/page/list?status=&amp;uName=&amp;requestIP=&amp;orgId=&amp;systemId=&amp;apiName=&amp;beginTime=2022-10-15+00:00:00&amp;endTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>apiName</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/log/page/list?status=&amp;uName=&amp;requestIP=&amp;orgId=&amp;systemId=&amp;apiName=&amp;beginTime=2022-10-15+00:00:00&amp;endTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>2022-10-15+00:00:00</Value>
        <MatchNames>
          <MatchName>beginTime</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/log/page/list?status=&amp;uName=&amp;requestIP=&amp;orgId=&amp;systemId=&amp;apiName=&amp;beginTime=2022-10-15+00:00:00&amp;endTime=2022-10-21+23:59:59&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>2022-10-21+23:59:59</Value>
        <MatchNames>
          <MatchName>endTime</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/dynamicRoutes/gateway-routes/routePage?routeId=&amp;isEbl=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>routeId</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/dynamicRoutes/gateway-routes/routePage?routeId=&amp;isEbl=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>isEbl</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/online?filter=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>filter</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/system/menuOpLog/save">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>\u7cfb\u7edf\u8d44\u6e90\u914d\u7f6e</Value>
        <MatchNames>
          <MatchName>[0]-&gt;"modelName"</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/sysresourcesconfig/list?code=&amp;name=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value />
        <MatchNames>
          <MatchName>name</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/sysresourcesconfig/list?code=&amp;name=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>1</Value>
        <MatchNames>
          <MatchName>pageNum</MatchName>
        </MatchNames>
      </Group>
      <Group LogicalName="" MatchType="Complete" Action="http://192.168.13.159:20086/sys/sysresourcesconfig/list?code=&amp;name=&amp;pageNum=1&amp;pageSize=10">
        <Name>Auto Detected</Name>
        <Selection>Ignore</Selection>
        <Value>10</Value>
        <MatchNames>
          <MatchName>pageSize</MatchName>
        </MatchNames>
      </Group>
    </FormFiller>
    <PlatformAuthentication>
      <Enabled>False</Enabled>
      <Domain />
      <Password Encrypted="false" />
      <UserName />
    </PlatformAuthentication>
    <ClientCertificateOption>
      <Option>2</Option>
    </ClientCertificateOption>
    <ClientSideCertificates>
      <ClientSideCertificate>
        <Enabled>False</Enabled>
        <FilePath />
        <Raw />
        <KeyPath />
        <Password Encrypted="false" />
        <InOldPemFormat>False</InOldPemFormat>
      </ClientSideCertificate>
    </ClientSideCertificates>
    <UserStoreCertificates />
  </UserInput>
</ScanConfiguration>