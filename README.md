# Compilador de Aplicativos Android

Compilador independente do MIA para projetos web (HTML, CSS e JavaScript) empacotados em APK Android.

## Como usar
1. Envie o ZIP do jogo para a pasta `entrada/` deste repositório.
2. O envio do ZIP para a branch `main` inicia automaticamente a compilação.
3. Abra **Actions** e selecione a execução **Compilar Desafio Lógico**.
4. Quando terminar, abra a execução e baixe o arquivo em **Artifacts**.

O ZIP deve conter um `index.html` e os arquivos locais usados pelo jogo (CSS, JavaScript, imagens, áudio etc.). O projeto é empacotado em um aplicativo Android com WebView.

## Observações
- Este repositório é público. Todo arquivo enviado para ele poderá ser visto e baixado por qualquer pessoa.
- Não envie chaves, senhas, dados pessoais ou projetos privados.
- O APK gerado fica disponível como artefato da execução do GitHub Actions por 7 dias.
- O primeiro build precisa ser validado com o ZIP real do jogo.
