import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Bases de armazenamento de dados', 'O Armazenamento de Dados é aplicado no Gerenciamento de Big Data e um fator-chave de sucesso em quase todas as empresas. Sem um data warehouse, nenhuma empresa hoje pode controlar seus processos e tomar as decisões certas em um nível estratégico, pois haveria falta de transparência de dados para todos os tomadores de decisão. Empresas maiores ainda têm vários data warehouses para diferentes propósitos. Gostaria também de explicar tópicos básicos sobre Engenharia de Dados e conceitos sobre bancos de dados e fluxos de dados.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Conceitos ACID vs BASE', 'Compreender bases de dados para armazenar, atualizar e analisar dados requer a compreensão de dois conceitos: ACID e BASE. Este é o primeiro artigo da série de artigos Data Warehousing Basics. As propriedades do ACID estão sendo aplicadas para bancos de dados a fim de cumprir os requisitos corporativos de confiabilidade e consistência. ACID é um acrônimo, e significa: Atomicidade – Cada transação é executada completamente ou não acontece de forma alguma. Se a transação não foi concluída, o processo reverte o banco de dados de volta ao estado antes do início da transação. Isso garante que todos os dados no banco de dados sejam válidos mesmo se executarmos grandes transações que incluem várias demonstrações (por exemplo.SQL) compostas em uma transação atualizando muitas linhas de dados no banco de dados. Se uma declaração falhar, toda a transação será abortada e, portanto, nenhuma alteração será feita. Consistência – Os bancos de dados são regidos por regras específicas definidas por formatos de tabela (tipos de dados) e relações de tabela, bem como outras funções como gatilhos. A consistência dos dados permanecerá confiável se as transações nunca colocarem em risco a integridade estrutural do banco de dados. Portanto, não é permitido salvar dados de diferentes tipos na mesma coluna única, usar valores de chave primária escritos novamente ou excluir dados de uma tabela que está estritamente relacionada aos dados em outra tabela. Isolamento – Bancos de dados são sistemas de vários usuários onde várias transações acontecem ao mesmo tempo. Com o Isolamento, as transações não podem comprometer a integridade de outras transações interagindo com elas enquanto ainda estão em andamento. Ele garante que as tabelas de dados estarão nos mesmos estados com várias transações acontecendo simultaneamente à medida que acontecem sequencialmente. Durabilidade – Os dados relacionados à transação concluída persistirão mesmo em casos de quedas de rede ou de energia. Bancos de dados que garantem a Durabilidade salvar dados inseridos ou atualizados permanentemente, salvar todas as transações executadas e planejadas em um registro e garantir a disponibilidade dos dados cometidos via transação mesmo após uma falha de energia ou outras falhas no sistema Se uma transação não for concluída com sucesso devido a uma falha técnica, ela não transformará os dados direcionados.') 
            )

connection.commit()
connection.close()