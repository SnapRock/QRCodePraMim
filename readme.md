# QRCodePraMim 💻📱

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  
**QRCodePraMim** é uma ferramenta simples e intuitiva para gerar QR Codes diretamente a partir de uma interface gráfica moderna. Feito com `PyQt5` para oferecer uma experiência visual elegante, você pode criar QR Codes personalizados e salvá-los como imagens PNG em poucos cliques.

## 🎯 Funcionalidades

- **Geração de QR Codes personalizados** para qualquer conteúdo (URLs, textos, informações de contato, etc.).
- **Salve o QR Code em formato PNG** diretamente no seu dispositivo.
- **Interface amigável e fácil de usar** baseada em `PyQt5`.

---

## 🚀 Demonstração de Uso

### Exemplo: Gerar QR Code para um website
Para gerar um QR Code para o site [Profusão Sonora](https://profusaosonora.com):

1. Execute o programa.
2. Insira o link **`https://profusaosonora.com`** no campo de texto.
3. Clique em "Gerar QR Code".
4. Visualize e salve o QR Code gerado!

### Exemplo: Gerar QR Code para um vCard
Para gerar um QR Code de um vCard com as seguintes informações:

```plaintext
BEGIN:VCARD
VERSION:3.0
FN:Comercial Retail Pro Brasil
ORG:Retail Pro Brasil
TEL:+55 11 97356-4216
EMAIL:contato@palatinoamericana.com
END:VCARD
```

1. Cole o conteúdo acima no campo de texto.
2. Clique em "Gerar QR Code".
3. O QR Code será gerado com os detalhes de contato prontos para uso!

---

## 🛠️ Instalação e Dependências

### Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado. Para instalar as dependências, use o comando:

```bash
pip install -r requirements.txt
```

### Como Executar

Para iniciar o aplicativo localmente, execute o arquivo principal:

```bash
python app_qrcode_pramim.py
```

---

## 🖥️ Gerando um Executável (Windows)

Se você deseja distribuir o aplicativo sem a necessidade de instalar o Python no sistema de destino, você pode gerar um executável único com **PyInstaller**.

1. Instale o **PyInstaller**:

```bash
pip install pyinstaller
```

2. Gere o executável:

```bash
pyinstaller --onefile --windowed app_qrcode_pramim.py
```

Isso criará um executável na pasta `dist/`, pronto para ser executado em qualquer máquina Windows.

## 📄 Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

