# xml-listify
Converts a tabbed text into XML `<list>` / `<list-item>`
Sample input:

```xml
<p>1. texto .... texto.</p>
<p> 2. texto .... texto.</p>
<p>     3. texto .... texto.</p>
<p>     3'. texto .... texto.</p>
<p>         4. texto .... texto.</p>
<p>         4’. texto .... texto.</p>
<p> 2’. texto .... texto.</p>
<p>     5. texto .... texto.</p>
<p>     5’. texto .... texto.</p>
<p>1'. texto .... texto.</p>
<p> 6. texto .... texto.</p>
<p> 6'. texto .... texto.</p>
<p>     7. texto .... texto.</p>
<p>         8. texto .... texto.</p>
<p>         8'. texto .... texto.</p>
<p>     7’. texto .... texto.</p>
<p>         9. texto .... texto.</p>
<p>         9'. texto .... texto.</p>
```

Sample output:
```xml
<list list-type="simple">
  <list-item><p>1. texto .... texto.</p></list-item>
  <list-item>
    <list list-type="simple">
      <list-item>   <p>2. texto .... texto.</p></list-item>
      <list-item>
        <list list-type="simple">
          <list-item>       <p>3. texto .... texto.</p></list-item>
          <list-item>       <p>3'. texto .... texto.</p></list-item>
          <list-item>
            <list list-type="simple">
              <list-item>           <p>4. texto .... texto.</p></list-item>
              <list-item>           <p>4\'. texto .... texto.</p></list-item>
            </list>
          </list-item>
        </list>
      </list-item>
      <list-item>   <p>2\'. texto .... texto.</p></list-item>
      <list-item>
        <list list-type="simple">
          <list-item>       <p>5. texto .... texto.</p></list-item>
          <list-item>       <p>5\'. texto .... texto.</p></list-item>
        </list>
      </list-item>
    </list>
  </list-item>
  <list-item><p>1'. texto .... texto.</p></list-item>
  <list-item>
``` 

# Comandos
Depois que você já tiver preparado o arquivo `chave.txt`, basta:
 1. `cdwin` comando para entrar na pasta xml do artigo.
 2. `lgp-listify -filename chave.txt`

Se a saída for parecida com o exemplo abaixo deve estar udo OK. Siga adiante para o passo 3.
```xml
<list list-type="simple">
  <list-item><p>1. texto .... texto.</p></list-item>
  <list-item>
    <list list-type="simple">
      <list-item>   <p>2. texto .... texto.</p></list-item>
      <list-item>
        <list list-type="simple">
          <list-item>       <p>3. texto .... texto.</p></list-item>
          <list-item>       <p>3'. texto .... texto.</p></list-item>
          <list-item>
            <list list-type="simple">
              <list-item>           <p>4. texto .... texto.</p></list-item>
              <list-item>           <p>4\'. texto .... texto.</p></list-item>
            </list>
          </list-item>
        </list>
      </list-item>
      <list-item>   <p>2\'. texto .... texto.</p></list-item>
      <list-item>
        <list list-type="simple">
          <list-item>       <p>5. texto .... texto.</p></list-item>
          <list-item>       <p>5\'. texto .... texto.</p></list-item>
        </list>
      </list-item>
    </list>
  </list-item>
  <list-item><p>1'. texto .... texto.</p></list-item>
  <list-item>
``` 
Finalize com o comando a seguir que criará o arquivo `chave.xml` com o conteúdo do comando anterior.
3. `lgp-listify -filename chave.txt > chave.xml` 
4. Substitua esse conteúdo no arquivo XML original do artigo.

# Preparação do arquivo `chave.txt`
## Arquivo DOC
No DOC a indentação deve estar:
 - usando TABS (→)
 - uma linha por parágrafo (¶)
 - cada linha com estilo `Paragraph` aplicado
```
[Paragraph]   |   1. texto .... texto.¶
[Paragraph]   |   →2. texto .... texto.¶
[Paragraph]   |   →→3. texto .... texto.¶
[Paragraph]   |   →→3'. texto .... texto.¶
[Paragraph]   |   →→→4. texto .... texto.¶
[Paragraph]   |   →→→4’. texto .... texto.¶
[Paragraph]   |   →2’. texto .... texto.¶
[Paragraph]   |   →→5. texto .... texto.¶
[Paragraph]   |   →→5’. texto .... texto.¶
[Paragraph]   |   1'. texto .... texto.¶
[Paragraph]   |   →6. texto .... texto.¶
[Paragraph]   |   →6'. texto .... texto.¶
[Paragraph]   |   →→7. texto .... texto.¶
[Paragraph]   |   →→→8. texto .... texto.¶
[Paragraph]   |   →→→8'. texto .... texto.¶
[Paragraph]   |   →→7’. texto .... texto.¶
[Paragraph]   |   →→→9. texto .... texto.¶
[Paragraph]   |   →→→9'. texto .... texto.¶
```

## Arquivo XML
Depois de exportar o XML deve estar com a mesma estrutura do DOC. Observar pois as vezes as linhas podem se quebrar e gerar erro. 

```xml
<p>1. texto .... texto.</p>
<p> 2. texto .... texto.</p>
<p>     3. texto .... texto.</p>
<p>     3'. texto .... texto.</p>
<p>         4. texto .... texto.</p>
<p>         4’. texto .... texto.</p>
<p> 2’. texto .... texto.</p>
<p>     5. texto .... texto.</p>
<p>     5’. texto .... texto.</p>
<p>1'. texto .... texto.</p>
<p> 6. texto .... texto.</p>
<p> 6'. texto .... texto.</p>
<p>     7. texto .... texto.</p>
<p>         8. texto .... texto.</p>
<p>         8'. texto .... texto.</p>
<p>     7’. texto .... texto.</p>
<p>         9. texto .... texto.</p>
<p>         9'. texto .... texto.</p>
```

## Arquivo `chave.txt`
Apenas as linhas do arquivo XML que contém os itens da chave devem ser copiados para um novo arquivo chamado `chave`.





