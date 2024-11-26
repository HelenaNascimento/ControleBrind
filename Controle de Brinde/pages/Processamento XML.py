import pandas_read_xml as pdx
from pandas_read_xml import flatten

# Carregar o XML com o namespace
namespace = {'': 'http://www.portalfiscal.inf.br/nfe'}  # Namespace para o XML

# Carregar o XML e verificar como os dados estão sendo lidos
df = pdx.read_xml('/home/technical/WorkSpace/ControleBrind/Controle de Brinde/pages/NFe.xml', ['NFe'])

# Imprimir a estrutura do DataFrame
print(df.head())
print(df.columns)
x