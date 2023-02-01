# Analisi dataset relativo all'inquinamento dell'aria

## Il dataset
Il dataset che andremo ad utilizzare è un dataset molto ricco di informazioni, ogni file, eccetto l’anno 2018, contiene oltre 200.000 righe. Quindi, abbiamo deciso di lavorare su una porzione dei file, prendendo in considerazione l’intervallo temporale che va dal 2008 al 2018. I campi che compongo il dataset sono:

<table>
<tr>
<td><b>Date:</b></td>
<td> questo campo contiene la data relativa al momento in cui è stato fatto il rilevamento. Il formato della data è composto dall’anno, il mese, il giorno, e l’ora.</td>
</tr>
<tr>
<td><b>BEN:</b></td>
<td> questo campo contiene il rilevamento del benzene. Il livello di benzene è misurato in μg/m³. Il benzene è un irritante per gli occhi e la pelle, lunghe esposizioni possono causare diversi tipi di cancro, leucemia e anemie. Il benzene è considerato un cancerogeno per l'uomo di gruppo 1 dalla IARC.</td>
</tr>
<tr>
<td><b>EBE:</b></td>
<td>
questo campo contiene il rilevamento dell’etilbenzene. Il livello di etilbenzene è misurato in μg/m³. L'esposizione a lungo termine può causare problemi all'udito o ai reni e l'IARC ha concluso che l'esposizione a lungo termine può produrre il cancro.</td>
</tr>
<tr>
<td><b>CO:</b></td>
<td>
questo campo contiene il rilevamento del monossido di carbonio. Il livello di monossido di carbonio è misurato in mg/m³. L'avvelenamento da monossido di carbonio comporta mal di testa, vertigini e confusione in brevi esposizioni e può provocare perdita di coscienza, aritmie, convulsioni o persino la morte a lungo termine.</td>
</tr>
<tr>
<td><b>NMHC:</b></td>
<td>
questo campo contiene il rilevamento di idrocarburi non metanici (composti organici volatili). Il livello di idrocarburi non metanici è misurato in mg/m³. L'esposizione prolungata ad alcune di queste sostanze può causare danni al fegato, ai reni e al sistema nervoso centrale. Si sospetta che alcuni di loro causino il cancro negli esseri umani.</td>
</tr>
<tr>
<td><b>NO:</b></td>
<td>
questo campo contiene il rilevamento dell’ossido nitrico. Il livello di ossido nitrico è misurato in μg/m³. Questo è un gas altamente corrosivo generato, tra l'altro, dai veicoli a motore e dai processi di combustione del carburante.</td>
</tr>
<tr>
<td><b>NO_2:</b></td>
<td>
questo campo contiene il rilevamento del biossido di azoto. Il livello di biossido di azoto è misurato in μg/m³. L'esposizione a lungo termine è causa di malattie polmonari croniche e sono dannose per la vegetazione.</td>
</tr>
<tr>
<td><b>O_3:</b></td>
<td>
questo campo contiene il rilevamento dell’ozono. Il livello di ozono è misurato in μg/m³. Livelli elevati possono produrre asma, bronchite o altre malattie polmonari croniche in gruppi sensibili o lavoratori all'aperto.</td>
</tr>
<tr>
<td><b>PM10:</b></td>
<td>
questo campo contiene il rilevamento del materiale particolato aerodisperso con particelle inferiori a 10 μm. Il livello di materiale particolato aerodisperso è misurato in μg/m³. Anche se non possono penetrare nell'alveolo, possono comunque penetrare attraverso i polmoni e colpire altri organi. L'esposizione a lungo termine può causare cancro ai polmoni e complicazioni cardiovascolari. </td>
</tr>
<tr>
<td><b>PM_25:</b></td>
<td>
questo campo contiene il rilevamento del materiale particolato aerodisperso, di diametro maggiore rispetto al precedente. Il livello di materiale particolato aerodisperso è misurato in μg/m³. Le dimensioni di queste particelle consentono loro di penetrare nelle regioni di scambio gassoso dei polmoni (alveoli) e persino di entrare nelle arterie. È stato dimostrato che l'esposizione a lungo termine è correlata al basso peso alla nascita e all'ipertensione nei neonati.
</td>
</tr>
<tr>
<td><b>SO_2:</b></td>
<td>
questo campo contiene il rilevamento dell’anidride solforosa. Il livello di anidride solforosa è misurato in μg/m³. Alti livelli di anidride solforosa possono produrre irritazione della pelle e delle membrane e peggiorare l'asma o le malattie cardiache nei gruppi sensibili.
</td>
</tr>
<tr>
<td><b>TCH:</b></td>
<td>
questo campo contiene il rilevamento del livello totale di idrocarburi. Questo livello totale di idrocarburi è misurato in mg/m³. Questo gruppo di sostanze può essere responsabile di diverse malattie del sangue, del sistema immunitario, del fegato, della milza, dei reni o dei polmoni.
</td> </tr>
<tr>
<td><b>TOL:</b></td>
<td>
questo campo contiene il rilevamento del toluene ( metilbenzene ). Il livello di toluene è misurato in μg/m³. L'esposizione a lungo termine a questa sostanza (presente anche nel fumo di tabacco) può causare complicazioni renali o danni permanenti al cervello.
</td> </tr>
<tr>
<td><b>Station:</b></td>
<td>	
questo campo contiene il codice identificativo della stazione che ha effettuato quel rilevamento. Nel dataset abbiamo una tabella `Station`, all’interno della quale sono contenuti i codici delle stazioni più altre informazioni molto importanti. Queste informazioni sono il nome della stazione, il nome del luogo dov’è situata e le indicazioni geografiche di questo luogo.
</td> </tr>
<tr>
<td><b>CH4:</b></td>
<td>
questo campo contiene il rilevamento del livello di metano. Il livello di metano è misurato in mg/m³. Questo gas è un asfissiante, che sostituisce l'ossigeno di cui gli animali hanno bisogno per respirare. Il metano può provocare vertigini, debolezza, nausea e perdita di coordinazione.
</td> </tr>
<tr>
<td><b>MXY:</b></td>
<td>
questo campo contiene il rilevamento del livello di m-xilene. Il livello di m-xilene è misurato in μg/m³. Gli xileni possono influenzare non solo l'aria, ma anche l'acqua e il suolo e una lunga esposizione a livelli elevati di xileni può provocare malattie che colpiscono il fegato, i reni e il sistema nervoso (in particolare la memoria e la reazione allo stimolo alterata).
</td> </tr>	
<tr>
<td><b>PXY:</b></td>
<td>
questo campo contiene il rilevamento del livello di p-xilene. Il livello di p-xilene è misurato in μg/m³. Vedere MXY per gli effetti dell'esposizione allo xilene sulla salute.
</td> </tr>
<tr>
<td><b>OXY:</b></td>
<td>
questo campo contiene il rilevamento del livello di o-xilene. Il livello di o-xilene è misurato in μg/m³. Vedere MXY per gli effetti dell'esposizione allo xilene sulla salute.
</td> </tr>
<tr>
<td><b>NOX:</b></td>
<td>
questo campo contiene il rilevamento del livello di ossidi di azoto. Il livello di ossidi di azoto è misurato in μg/m³. Colpiscono il sistema respiratorio umano peggiorando l'asma o altre malattie, e sono responsabili del colore bruno-giallastro dello smog fotochimico.

</table>

[Link](https://www.kaggle.com/datasets/decide-soluciones/air-quality-madrid) al dataset su kaggle

## Fase di ETL
Per poter proseguire con il nostro progetto abbiamo dovuto eseguire una fase di ETL (*Extraction, Transfor-mation, Load*).

Come prima cosa abbiamo analizzato i dati visivamente, per capire se tutti i file del nostro dataset erano conformi tra di loro e non presentavano anomalie, poi abbiamo effettuato la vera e propria "pulizia dei dati". 

Il dataset era composto da un file CSV per ogni anno, quindi, per una maggiore comodità abbiamo deciso di unificare tale csv in un unico dataframe.

## Analisi Descrittiva
Durante lo step successivo andremo a realizzare delle analisi di tipo descrittivo. Le analisi descrittive, così come suggerisce il nome, sintetizzano o descrivono i dati e creano dei risultati che sono interpretabili dagli esseri umani. I valori risultati più interessanti da studiare sono risultati quelli relativi al biossido di azoto, ossido nitrico, PM10, PM25 e anidride solforosa.
![](https://github.com/ChiaraAmalia/DataScience2Project/blob/main/img_doc/rilevanza_agenti_inquinanti.png)
Percentuali significative corrispondono al PM10 e al NO, i quali, insieme, raggiungono il 40% del totale.

## Distribuzioni
Lo step successivo è stato quello di valutare la distribuzione della concentrazione degli agenti inquinanti più significativi, presenti all’interno del dataset.

## Analisi Temporali
In questa analisi siamo andati quindi a visualizzare l'andamento temporale dei vari agenti chimici presenti nell'aria.

## Analisi Geografiche 
In questa anlisi siamo andati a visualizzare la concentrazione di inquinamento in ciascuna area della città, riportando risulati significativi soprattutto nelle zone industriali.

## Clustering
Prima di descrivere i risultati ottenuti tramite le varie tecniche di clustering, occorre specificare quali sono state le azioni fatte sul dataset per ottenere tali risultati. Il primo algoritmo utilizzato è stato i K-means, il quale, lavorando sulle distanze non ammetteva valori Nan. Abbiamo valutato se eliminare direttamente tali valori, oppure, se sostituirli con una media troncata. Il dataset presenta alcune problematiche relative alla presenza di valori Nan, ad esempio abbiamo il problema che alcune stazioni, per un mese, o per lunghi inter-valli di tempo, non hanno misurato un certo agente inquinante, oppure, lo hanno misurato pochissime volte. Nel calcolo della media troncata abbiamo operato due suddivisioni per ottenere un valore molto preciso. Noi calcolavamo per ogni agente inquinante usato per l’analisi, abbiamo preso i singoli anni, e per ogni anno abbiamo considerato le singole stazioni.
A causa della presenza di troppi valori Nan, o solo valori Nan, la funzione usata per il calcolo della media troncata restituiva un valore Nan. Quindi, abbiamo dovuto utilizzare un valore medio più ampio, che era quello annuale. Questa soluzione generava una nuova problematica, infatti, i punti non erano più distribuiti in maniera omogenea, avevamo dei fasci di punti con un parametro costante, e questo sbilanciava i cluster. Di conseguenza abbiamo scelto di procedere con un approccio ibrido, cioè, dove possibile sostituiamo i Nan con le medie troncate. Dove ciò non è possibile procediamo con la rimozione del valore.
La seconda operazione che è stata fatta è relativa solo a due algoritmi di clustering, il gerarchico e il DBSCAN. Abbiamo dovuto ridurre le dimensioni del dataset per motivi computazionali e di tempo. Infatti, lavorando in un ambiente locale non è possibile eseguire quest’analisi su dataset con oltre un milione di righe, quindi abbiamo estratto casualmente elementi da ogni singolo anno del dataset e, mettendoli insieme, abbiamo ottenuto un nuovo dataset. Come prima operazione di clustering abbiamo preso in considerazione i campi relativi al biossido di azoto (NO_2) e l’anidride solforosa (SO_2). Si è deciso poi di effettuare un'ulteriore operazione di clustering, prendendo in considerazione una nuova coppia di agenti inquinanti, ovvero PM10 e SO_2.
  
### PCA
Si è inoltre effettuata un’operazione di clustering sfruttando tutti i principali agenti inquinanti. Per farlo ab-biamo utilizzato La PCA, che sta per “principal component analysis”. Questa è una tecnica per la semplifica-zione dei dati utilizzata nell’ambito del machine learning. Questa tecnica ha lo scopo di ridurre il numero di features che descrivono un insieme di dati. Queste tecniche vengono implementate limitando il più possibile la perdita di informazioni.
  
## Classificazione
In questa sezione sono riportate le analisi effettuate attraverso le tecniche di classificazione, utilizzando mo-delli predittivi. L’obiettivo di questa analisi è quello di confrontare le prestazioni in termini di accuratezza di diversi modelli di classificazione, addestrati su un sottoinsieme del dataset originario, per poi testarlo sul restante sottoinsieme del dataset. Essendo il nostro dataset composto da dati raccolti dal 2008 al 2018, ab-biamo deciso di addestrare il modello con i dati raccolti fino al 2016 e testarlo quindi con i dati dal 2017 al 2018.
L’accuratezza di un modello di classificazione è intesa come il rapporto tra il numero di dati classificati cor-rettamente e il numero totale dei dati sottoposti a classificazione.
Per definire il modello sono stati utilizzati degli algoritmi messi a disposizione dalla libreria Scikit-Learn di Python. Si è deciso di effettuare due tipologie di classificazione:
<ul>
  <li>Binaria, relativamente al parametro PM10, in base alle classi Tollerabile/Non Tollerabile</li>
  <li>Multi-classe, relativamente al parametro NO_2, nelle classi Tollerabile/Parzialmente Tollerabile/Non Tollerabile</li>
</ul>
  
## Serie Temporali
In questa fase di analisi si è proceduto all'utilizzo delle serie temporali mediante la visualizzazione di trend e previsioni che possono essere realizzate con specifici algoritmi. Nella fase di ETL è risultato anche in questo caso necessario il trattamento dei valori considerando una media giornaliera di essi, per ciascun agente, di seguito anche mensile. Si è deciso di effettuare le seguenti analisi (effettuate sia raggruppando i dati giornalmente che mensilmente):
<ul>
  <li>Stazionarietà</li>
  <li>Autocorrelazione e correlazione parziale</li>
  <li>Modello ARIMA</li>
  <li>Predizione in-sample</li>
  <li>Metriche di valutazione: MAE, MAPE, MSE, R-squared</li>
  <li>Predizione out-sample</li>
</ul>

## Tecnologie utilizzate
<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>Sklearn</li>
  <li>Seaborn</li>
  <li>Statsmodel</li>
  <li>Matplotlib</li>
</ul>

Ulteriori dettagli relativi alle analisi effettuate sono riportati nella seguente [relazione](https://github.com/ChiaraAmalia/DataScience2Project/blob/main/Relazione_Classificazione_Regressione_SerieTemporali.pdf)
