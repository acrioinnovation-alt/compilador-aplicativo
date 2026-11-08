# Compilador Android privado do MIA

Este repositório público contém somente o código do compilador. **Não envie ZIPs de jogos ou aplicativos para este repositório.**

O MIA inicia a compilação por uma solicitação temporária autenticada:
1. O MIA entrega o ZIP ao runner por HTTPS, usando um token temporário de uso único.
2. O runner prepara e compila o aplicativo.
3. O APK é transferido de volta ao armazenamento privado do MIA, com outro token temporário.
4. O runner apaga os arquivos de trabalho ao final.

Este fluxo não publica ZIPs, APKs ou artefatos de compilação no GitHub. O APK é disponibilizado ao usuário somente pelo MIA, com a chave privada daquele projeto.

O workflow deste repositório deve ser iniciado pelo MIA. Não use o botão de execução manual para projetos reais.
