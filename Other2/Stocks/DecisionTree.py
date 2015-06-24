import requests
import math
def decision(s):
	score = 0 #higher score means more attractive investment
	for n in s: #s is our dictionary of variables
		if s[n][0] >= s[n][1]: #check to see if value is above cutoff
			score = score + s[n][2] #adding signifance level to score
		else: 
			score = score - s[n][2] #subtracting significance level to score
	if score > .5: #score level above which we decide to invest
		return "yes"
	else:
		return "no"
	
comb = {"supply" : [2,7,.1], "silver" : [1000,750,.5],\
"inflation" : [.07,.015,.2], "copper" : [223,3432,.2]} #example variables (can use any number of variables)
print decision(comb) #prints whether we should invest

# ex, get_raw_dict('GOOG', '2009-09-11', '2010-03-10') i.e. date is yyyy-mm-dd, most recent date first in list
def get_raw_dict(ticker, st, end):
	site = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.historicaldata%20where%20symbol%20%3D%20%22" + ticker + "%22%20and%20startDate%20%3D%20%22" + st + "%22%20and%20endDate%20%3D%20%22" + end + "%22&format=json&env=http%3A%2F%2Fdatatables.org%2Falltables.env"
	raw_data = requests.get(site)
	raw_json = raw_data.json()
	# list of dictionaries of the form Volume, Adj_Close, High, Date (yyyy-mm-dd), Low, date, Close, Open
	return ticker, raw_json['query']['results']['quote']

# return a list of tuples of the form (date, closing price), with most recent date first in output list
def get_closes_tup(input_dict):
	ans = []
	for day in input_dict:
		ans.append((day['Date'], day['Close']))
	return ans

# return a list of closing prices, with the most recent close first
def get_closes(input_dict):
	ans = []
	for day in input_dict:
		ans.append(float(day['Close']))
	return ans

# returns the mean of a list of floats (just the prices)
def mean(lst):
	return sum(lst)/len(lst)

def standard_dev(lst):
	avg = mean(lst)
	variance = map(lambda x: (x-avg)**2, lst)
	return math.sqrt(sum(variance)/(len(variance)-1))

def allstocks(ticker, st, end):
	for stock in stocks:
		try:
			print get_raw_dict(stock, st, end)
		except Exception:
			pass
	

stocks = ['A', 'AA', 'AAN', 'AAON', 'AAP', 'AAPL'] # 'AAT', 'AATI', 'AAWW', 'ABAX', 'ABBC', 'ABC', 'ABCB', 'ABCD', 'ABCO', 'ABFS', 'ABG', 'ABM', 'ABMD', 'ABT', 'ABVT', 'ACAS', 'ACAT', 'ACC', 'ACCL', 'ACCO', 'ACE', 'ACET', 'ACGL', 'ACHN', 'ACI', 'ACIW', 'ACLS', 'ACM', 'ACN', 'ACO', 'ACOM', 'ACOR', 'ACPW', 'ACTG', 'ACTV', 'ACUR', 'ACW', 'ACXM', 'ADBE', 'ADC', 'ADI', 'ADM', 'ADP', 'ADPI', 'ADS', 'ADSK', 'ADTN', 'ADVS', 'AEA', 'AEC', 'AEE', 'AEGR', 'AEIS', 'AEL', 'AEO', 'AEP', 'AEPI', 'AES', 'AET', 'AF', 'AFAM', 'AFCE', 'AFFX', 'AFFY', 'AFG', 'AFL', 'AFP', 'AFSI', 'AGCO', 'AGII', 'AGL', 'AGM', 'AGN', 'AGNC', 'AGO', 'AGP', 'AGX', 'AGYS', 'AH', 'AHC', 'AHL', 'AHS', 'AHT', 'AI', 'AIG', 'AIMC', 'AIN', 'AINV', 'AIQ', 'AIR', 'AIRM', 'AIS', 'AIT', 'AIV', 'AIZ', 'AJG', 'AKAM', 'AKR', 'AKRX', 'AKS', 'AL', 'ALB', 'ALC', 'ALCO', 'ALE', 'ALEX', 'ALG', 'ALGN', 'ALGT', 'ALIM', 'ALJ', 'ALK', 'ALKS', 'ALL', 'ALNC', 'ALNY', 'ALOG', 'ALR', 'ALSK', 'ALTE', 'ALTH', 'ALTR', 'ALV', 'ALX', 'ALXN', 'AM', 'AMAG', 'AMAT', 'AMCC', 'AMD', 'AME', 'AMED', 'AMG', 'AMGN', 'AMKR', 'AMLN', 'AMN', 'AMP', 'AMPE', 'AMR', 'AMRC', 'AMRI', 'AMRS', 'AMSC', 'AMSF', 'AMSG', 'AMSWA', 'AMT', 'AMTD', 'AMWD', 'AMZN', 'AN', 'ANAC', 'ANAD', 'ANAT', 'ANDE', 'ANEN', 'ANF', 'ANGO', 'ANH', 'ANN', 'ANR', 'ANSS', 'ANTH', 'ANV', 'AOI', 'AOL', 'AON', 'AONE', 'AOS', 'AOSL', 'AP', 'APA', 'APAC', 'APAGF', 'APC', 'APD', 'APEI', 'APH', 'APKT', 'APOG', 'APOL', 'ARAY', 'ARB', 'ARBA', 'ARC', 'ARCC', 'ARCL', 'ARDNA', 'ARE', 'AREX', 'ARG', 'ARGN', 'ARI', 'ARIA', 'ARII', 'ARJ', 'ARNA', 'ARO', 'AROW', 'ARQL', 'ARR', 'ARRS', 'ARRY', 'ART', 'ARTC', 'ARTNA', 'ARUN', 'ARW', 'ARX', 'ASBC', 'ASCA', 'ASCMA', 'ASEI', 'ASGN', 'ASH', 'ASI', 'ASNA', 'ASTE', 'ASYS', 'AT', 'ATEC', 'ATHN', 'ATI', 'ATK', 'ATLO', 'ATMI', 'ATML', 'ATNI', 'ATO', 'ATPG', 'ATR', 'ATRC', 'ATRI', 'ATRO', 'ATSG', 'ATU', 'ATVI', 'ATW', 'ATX', 'AUMN', 'AUXL', 'AVA', 'AVAV', 'AVB', 'AVD', 'AVEO', 'AVGO', 'AVID', 'AVII', 'AVNR', 'AVNW', 'AVP', 'AVT', 'AVTR', 'AVX', 'AVY', 'AWH', 'AWI', 'AWK', 'AWR', 'AXAS', 'AXE', 'AXL', 'AXP', 'AXS', 'AXTI', 'AYI', 'AYR', 'AZO', 'AZPN', 'AZZ', 'B', 'BA', 'BABY', 'BAC', 'BAGL', 'BAH', 'BALT', 'BANF', 'BANRD', 'BARI', 'BAS', 'BAX', 'BBBB', 'BBBY', 'BBG', 'BBND', 'BBNK', 'BBOX', 'BBRG', 'BBSI', 'BBT', 'BBW', 'BBY', 'BC', 'BCO', 'BCPC', 'BCR', 'BCRX', 'BCSI', 'BDC', 'BDE', 'BDGE', 'BDN', 'BDX', 'BEAT', 'BEAV', 'BEBE', 'BEC', 'BECN', 'BEE', 'BELFB', 'BEN', 'BEXP', 'BF.B', 'BFIN', 'BFS', 'BG', 'BGC', 'BGCP', 'BGFV', 'BGG', 'BGMD', 'BGS', 'BH', 'BHE', 'BHI', 'BHLB', 'BID', 'BIG', 'BIIB', 'BIO', 'BIOS', 'BIRT', 'BJ', 'BJRI', 'BK', 'BKCC', 'BKD', 'BKE', 'BKH', 'BKI', 'BKMU', 'BKR', 'BKS', 'BKU', 'BKYF', 'BLC', 'BLDR', 'BLK', 'BLKB', 'BLL', 'BLT', 'BLTI', 'BLUD', 'BLX', 'BMC', 'BMI', 'BMR', 'BMRC', 'BMRN', 'BMS', 'BMTC', 'BMTI', 'BMY', 'BNCL', 'BNHNA', 'BOBE', 'BODY', 'BOFI', 'BOH', 'BOKF', 'BONE', 'BONT', 'BOOM', 'BOX', 'BPAX', 'BPFH', 'BPI', 'BPOP', 'BPZ', 'BR', 'BRC', 'BRCD', 'BRCM', 'BRE', 'BRK.B', 'BRKL', 'BRKR', 'BRKS', 'BRLI', 'BRO', 'BRS', 'BRY', 'BSFT', 'BSRR', 'BSTC', 'BSX', 'BTH', 'BTU', 'BTX', 'BUCY', 'BUSE', 'BWA', 'BWC', 'BWEN', 'BWINB', 'BWLD', 'BWS', 'BXP', 'BXS', 'BYD', 'BYI', 'BZ', 'BZH', 'C', 'CA', 'CAB', 'CAC', 'CACB', 'CACC', 'CACI', 'CADX', 'CAG', 'CAH', 'CAK', 'CAKE', 'CALD', 'CALM', 'CALP', 'CALX', 'CAM', 'CAP', 'CAR', 'CAS', 'CASC', 'CASS', 'CASY', 'CAT', 'CATM', 'CATO', 'CATY', 'CAVM', 'CB', 'CBB', 'CBE', 'CBEY', 'CBG', 'CBI', 'CBK', 'CBKN', 'CBL', 'CBLI', 'CBM', 'CBNJ', 'CBOE', 'CBOU', 'CBR', 'CBRL', 'CBRX', 'CBS', 'CBSH', 'CBST', 'CBT', 'CBU', 'CBZ', 'CCBG', 'CCC', 'CCE', 'CCF', 'CCG', 'CCI', 'CCIX', 'CCK', 'CCL', 'CCMP', 'CCNE', 'CCO', 'CCOI', 'CCRN', 'CDE', 'CDI', 'CDNS', 'CDR', 'CDXS', 'CDZI', 'CE', 'CEC', 'CECO', 'CEDC', 'CEG', 'CELG', 'CELL', 'CENTA', 'CENX', 'CEPH', 'CERN', 'CERS', 'CETV', 'CEVA', 'CF', 'CFFN', 'CFN', 'CFNB', 'CFNL', 'CFR', 'CFX', 'CGI', 'CGNX', 'CGX', 'CHCO', 'CHD', 'CHDN', 'CHDX', 'CHE', 'CHFC', 'CHFN', 'CHG', 'CHH', 'CHK', 'CHKE', 'CHMT', 'CHRS', 'CHRW', 'CHS', 'CHSI', 'CHSP', 'CHTP', 'CHTR', 'CHUX', 'CI', 'CIA', 'CIE', 'CIEN', 'CIGX', 'CIM', 'CINF', 'CIR', 'CIT', 'CIX', 'CKH', 'CKP', 'CL', 'CLB', 'CLC', 'CLD', 'CLDT', 'CLDX', 'CLF', 'CLFC', 'CLGX', 'CLH', 'CLI', 'CLMS', 'CLNE', 'CLNY', 'CLP', 'CLR', 'CLUB', 'CLW', 'CLWR', 'CLX', 'CMA', 'CMC', 'CMCO', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMLS', 'CMN', 'CMO', 'CMP', 'CMRG', 'CMS', 'CMTL', 'CNA', 'CNBC', 'CNBKA', 'CNC', 'CNH', 'CNK', 'CNL', 'CNMD', 'CNO', 'CNP', 'CNQR', 'CNS', 'CNSL', 'CNU', 'CNVO', 'CNW', 'CNX', 'COBZ', 'COCO', 'CODE', 'CODI', 'COF', 'COG', 'COH', 'COHR', 'COHU', 'COKE', 'COL', 'COLB', 'COLM', 'CONN', 'COO', 'COP', 'COR', 'CORE', 'CORT', 'COST', 'COV', 'COWN', 'CPA', 'CPB', 'CPE', 'CPF', 'CPHD', 'CPK', 'CPKI', 'CPLA', 'CPN', 'CPO', 'CPRT', 'CPSI', 'CPST', 'CPT', 'CPTS', 'CPWM', 'CPWR', 'CPX', 'CQB', 'CR', 'CRAI', 'CRAY', 'CRD.B', 'CRDN', 'CREE', 'CRI', 'CRIS', 'CRK', 'CRL', 'CRM', 'CRMT', 'CROX', 'CRR', 'CRRC', 'CRS', 'CRTX', 'CRUS', 'CRVL', 'CRWN', 'CRY', 'CRZO', 'CSA', 'CSBK', 'CSC', 'CSCO', 'CSE', 'CSFL', 'CSGP', 'CSGS', 'CSH', 'CSII', 'CSL', 'CSOD', 'CSS', 'CSTR', 'CSU', 'CSWC', 'CSX', 'CTAS', 'CTB', 'CTBI', 'CTCT', 'CTGX', 'CTIC', 'CTL', 'CTO', 'CTRN', 'CTS', 'CTSH', 'CTWS', 'CTXS', 'CUB', 'CUZ', 'CV', 'CVA', 'CVBF', 'CVC', 'CVCO', 'CVD', 'CVG', 'CVGI', 'CVGW', 'CVH', 'CVI', 'CVLT', 'CVO', 'CVS', 'CVTI', 'CVX', 'CW', 'CWCO', 'CWEI', 'CWH', 'CWST', 'CWT', 'CWTR', 'CXO', 'CXPO', 'CXS', 'CXW', 'CY', 'CYBX', 'CYH', 'CYMI', 'CYN', 'CYNO', 'CYS', 'CYT', 'CYTX', 'CZNC', 'D', 'DAKT', 'DAL', 'DAN', 'DAR', 'DBD', 'DCI', 'DCO', 'DCOM', 'DCT', 'DCTH', 'DD', 'DDD', 'DDIC', 'DDR', 'DDS', 'DE', 'DECK', 'DEI', 'DEL', 'DELL', 'DENN', 'DEPO', 'DEST', 'DF', 'DFG', 'DFR', 'DFS', 'DFT', 'DFZ', 'DG', 'DGI', 'DGICA', 'DGII', 'DGIT', 'DGX', 'DHI', 'DHIL', 'DHR', 'DHT', 'DHX', 'DIN', 'DIOD', 'DIS', 'DISCA', 'DISH', 'DK', 'DKS', 'DLA', 'DLB', 'DLGC', 'DLLR', 'DLR', 'DLTR', 'DLX', 'DM', 'DMAN', 'DMD', 'DMND', 'DMRC', 'DNB', 'DNBK', 'DNDN', 'DNR', 'DO', 'DOLE', 'DORM', 'DOV', 'DOW', 'DOX', 'DPL', 'DPS', 'DPZ', 'DRC', 'DRCO', 'DRE', 'DRH', 'DRI', 'DRIV', 'DRL', 'DRQ', 'DRRX', 'DSPG', 'DST', 'DSW', 'DTE', 'DTG', 'DTSI', 'DTV', 'DUF', 'DUK', 'DUSA', 'DV', 'DVA', 'DVAX', 'DVN', 'DVOX', 'DVR', 'DW', 'DWA', 'DWSN', 'DX', 'DXCM', 'DXPE', 'DY', 'DYAX', 'DYN', 'EAT', 'EBAY', 'EBF', 'EBIX', 'EBS', 'EBSB', 'EBTC', 'EBTX', 'ECHO', 'ECL', 'ECOL', 'ECPG', 'ECYT', 'ED', 'EDE', 'EDMC', 'EDR', 'EE', 'EEFT', 'EF', 'EFII', 'EFSC', 'EFX', 'EGBN', 'EGHT', 'EGLE', 'EGN', 'EGOV', 'EGP', 'EGY', 'EHTH', 'EIG', 'EIX', 'EK', 'EL', 'ELGX', 'ELLI', 'ELMG', 'ELNK', 'ELON', 'ELRC', 'ELS', 'ELX', 'ELY', 'EM', 'EMAN', 'EMC', 'EMCI', 'EME', 'EMKR', 'EMN', 'EMR', 'END', 'ENDP', 'ENH', 'ENOC', 'ENR', 'ENS', 'ENSG', 'ENTG', 'ENTR', 'ENV', 'ENZ', 'ENZN', 'EOG', 'EP', 'EPAX', 'EPAY', 'EPHC', 'EPIQ', 'EPL', 'EPM', 'EPOC', 'EPR', 'EQIX', 'EQR', 'EQT', 'EQY', 'ERIE', 'ERII', 'ERT', 'ERTS', 'ES', 'ESBF', 'ESC', 'ESE', 'ESGR', 'ESI', 'ESIO', 'ESL', 'ESRX', 'ESS', 'ESSA', 'ESSX', 'ETFC', 'ETH', 'ETM', 'ETN', 'ETR', 'EV', 'EVC', 'EVR', 'EW', 'EWBC', 'EXAC', 'EXAM', 'EXAR', 'EXAS', 'EXBD', 'EXC', 'EXEL', 'EXH', 'EXL', 'EXLS', 'EXM', 'EXP', 'EXPD', 'EXPE', 'EXPO', 'EXPR', 'EXR', 'EXTR', 'EXXI', 'EZPW', 'F', 'FAF', 'FALC', 'FARM', 'FARO', 'FAST', 'FBC', 'FBCM', 'FBN', 'FBNC', 'FC', 'FCBC', 'FCE.A', 'FCEL', 'FCF', 'FCFS', 'FCH', 'FCN', 'FCNCA', 'FCS', 'FCX', 'FDEF', 'FDML', 'FDO', 'FDP', 'FDS', 'FDX', 'FE', 'FEIC', 'FELE', 'FF', 'FFBC', 'FFCH', 'FFG', 'FFIC', 'FFIN', 'FFIV', 'FFN', 'FHCO', 'FHN', 'FIBK', 'FICO', 'FII', 'FINL', 'FIRE', 'FIS', 'FISI', 'FISV', 'FITB', 'FIX', 'FIZZ', 'FL', 'FLDM', 'FLIC', 'FLIR', 'FLO', 'FLOW', 'FLR', 'FLS', 'FLT', 'FLWS', 'FMBI', 'FMC', 'FMD', 'FMER', 'FN', 'FNB', 'FNF', 'FNFG', 'FNGN', 'FNLC', 'FNSR', 'FO', 'FOE', 'FOLD', 'FOR', 'FORM', 'FORR', 'FOSL', 'FPIC', 'FPO', 'FPTB', 'FR', 'FRC', 'FRED', 'FRF', 'FRM', 'FRME', 'FRNK', 'FRO', 'FRP', 'FRPT', 'FRT', 'FRX', 'FSC', 'FSCI', 'FSII', 'FSL', 'FSLR', 'FSP', 'FSR', 'FSS', 'FST', 'FSTR', 'FSYS', 'FTEK', 'FTI', 'FTK', 'FTNT', 'FTO', 'FTR', 'FUBC', 'FUL', 'FULT', 'FUR', 'FURX', 'FVE', 'FWRD', 'FXCB', 'FXCM', 'FXEN', 'G', 'GABC', 'GAIN', 'GAS', 'GB', 'GBCI', 'GBDC', 'GBL', 'GBLI', 'GBX', 'GCA', 'GCAP', 'GCI', 'GCO', 'GCOM', 'GD', 'GDI', 'GDOT', 'GDP', 'GE', 'GEF', 'GEN', 'GEO', 'GEOI', 'GEOY', 'GERN', 'GES', 'GET', 'GEVO', 'GFF', 'GFIG', 'GGC', 'GGG', 'GGP', 'GGS', 'GHDX', 'GHL', 'GHM', 'GIFI', 'GIII', 'GILD', 'GIS', 'GKNT', 'GKSR', 'GLAD', 'GLBC', 'GLBL', 'GLCH', 'GLDD', 'GLF', 'GLNG', 'GLPW', 'GLRE', 'GLT', 'GLUU', 'GLW', 'GM', 'GMAN', 'GMCR', 'GME', 'GMO', 'GMR', 'GMT', 'GMXR', 'GNC', 'GNCMA', 'GNET', 'GNK', 'GNOM', 'GNRC', 'GNTX', 'GNW', 'GOK', 'GOOD', 'GOOG', 'GORO', 'GOV', 'GPC', 'GPI', 'GPK', 'GPN', 'GPOR', 'GPRE', 'GPRO', 'GPS', 'GPX', 'GR', 'GRA', 'GRB', 'GRC', 'GRIF', 'GRM', 'GRMN', 'GRT', 'GS', 'GSAT', 'GSBC', 'GSIG', 'GSIT', 'GSM', 'GSOL', 'GSS', 'GST', 'GT', 'GTI', 'GTIV', 'GTLS', 'GTN', 'GTS', 'GTXI', 'GTY', 'GUID', 'GVA', 'GWR', 'GWW', 'GXP', 'GY', 'H', 'HA', 'HAE', 'HAFC', 'HAIN', 'HAL', 'HALL', 'HALO', 'HANS', 'HAR', 'HAS', 'HAYN', 'HBAN', 'HBHC', 'HBI', 'HBIO', 'HCA', 'HCBK', 'HCC', 'HCCI', 'HCKT', 'HCN', 'HCP', 'HCSG', 'HD', 'HDY', 'HE', 'HEES', 'HEI', 'HEK', 'HELE', 'HERO', 'HES', 'HEV', 'HF', 'HFWA', 'HGG', 'HGIC', 'HGR', 'HGSI', 'HHC', 'HHGP', 'HHS', 'HI', 'HIBB', 'HIG', 'HII', 'HIL', 'HILL', 'HITK', 'HITT', 'HIW', 'HK', 'HL', 'HLF', 'HLIT', 'HLS', 'HLX', 'HMA', 'HME', 'HMN', 'HMPR', 'HMSY', 'HNH', 'HNI', 'HNR', 'HNRG', 'HNSN', 'HNT', 'HNZ', 'HOC', 'HOG', 'HOLX', 'HOMB', 'HOME', 'HON', 'HOOK', 'HOS', 'HOT', 'HOTT', 'HOV', 'HP', 'HPP', 'HPQ', 'HPT', 'HPY', 'HR', 'HRB', 'HRC', 'HRG', 'HRL', 'HRS', 'HS', 'HSC', 'HSIC', 'HSII', 'HSNI', 'HSP', 'HST', 'HSTM', 'HSY', 'HT', 'HTBK', 'HTCO', 'HTGC', 'HTH', 'HTLD', 'HTLF', 'HTS', 'HTWR', 'HTZ', 'HUB.B', 'HUBG', 'HUM', 'HUN', 'HURC', 'HURN', 'HUSA', 'HUVL', 'HVT', 'HW', 'HWAY', 'HWCC', 'HWKN', 'HXL', 'HYC', 'HZO', 'IACI', 'IART', 'IBI', 'IBKC', 'IBKR', 'IBM', 'IBOC', 'ICE', 'ICFI', 'ICGE', 'ICLK', 'ICOG', 'ICON', 'ICUI', 'ID', 'IDA', 'IDCC', 'IDIX', 'IDT', 'IDTI', 'IDXX', 'IEX', 'IFF', 'IFSIA', 'IFT', 'IGT', 'IGTE', 'IHC', 'IHS', 'IIIN', 'IILG', 'IIVI', 'IL', 'ILMN', 'IM', 'IMGN', 'IMKTA', 'IMMR', 'IMMU', 'IMN', 'IN', 'INAP', 'INCY', 'INDB', 'INFA', 'INFI', 'INFN', 'INHX', 'ININ', 'INN', 'INSM', 'INSP', 'INSU', 'INT', 'INTC', 'INTL', 'INTU', 'INTX', 'INVE', 'INWK', 'IO', 'IOSP', 'IP', 'IPAR', 'IPCC', 'IPCM', 'IPG', 'IPGP', 'IPHI', 'IPHS', 'IPI', 'IPSU', 'IPXL', 'IR', 'IRBT', 'IRC', 'IRDM', 'IRET', 'IRF', 'IRIS', 'IRM', 'IRWD', 'ISBC', 'ISCA', 'ISH', 'ISIL', 'ISIS', 'ISLE', 'ISRG', 'ISRL', 'ISSI', 'ISTA', 'ISYS', 'IT', 'ITC', 'ITG', 'ITMN', 'ITRI', 'ITT', 'ITW', 'IVAC', 'IVC', 'IVR', 'IVZ', 'IXYS', 'JACK', 'JAG', 'JAH', 'JAKK', 'JAZZ', 'JBHT', 'JBL', 'JBLU', 'JBT', 'JCI', 'JCOM', 'JCP', 'JCS', 'JDAS', 'JDSU', 'JEC', 'JEF', 'JJSF', 'JKHY', 'JLL', 'JMBA', 'JMP', 'JNJ', 'JNPR', 'JNS', 'JNY', 'JOE', 'JOSB', 'JOUT', 'JOYG', 'JPM', 'JRCC', 'JRN', 'JW.A', 'JWN', 'K', 'KAI', 'KALU', 'KAMN', 'KAR', 'KBALB', 'KBH', 'KBR', 'KBW', 'KCAP', 'KCG', 'KCI', 'KCLI', 'KCP', 'KDN', 'KEG', 'KELYA', 'KEM', 'KERX', 'KEX', 'KEY', 'KEYN', 'KEYW', 'KFRC', 'KFT', 'KFY', 'KIM', 'KIRK', 'KITD', 'KKD', 'KLAC', 'KLIC', 'KMB', 'KMGB', 'KMI', 'KMT', 'KMX', 'KND', 'KNDL', 'KNL', 'KNOL', 'KNOT', 'KNSY', 'KNX', 'KNXA', 'KO', 'KOG', 'KOP', 'KOPN', 'KOS', 'KR', 'KRA', 'KRC', 'KRG', 'KRNY', 'KRO', 'KS', 'KSS', 'KSU', 'KSWS', 'KTOS', 'KV.A', 'KVHI', 'KW', 'KWK', 'KWR', 'L', 'LABL', 'LAD', 'LAMR', 'LANC', 'LAVA', 'LAWS', 'LAYN', 'LAZ', 'LB', 'LBAI', 'LBTYA', 'LBY', 'LCAPA', 'LCC', 'LCI', 'LCRY', 'LCUT', 'LDL', 'LDR', 'LEA', 'LEAP', 'LECO', 'LEG', 'LEN', 'LF', 'LFUS', 'LG', 'LGF', 'LGND', 'LH', 'LHCG', 'LHO', 'LIFE', 'LII', 'LINC', 'LINTA', 'LIOX', 'LIZ', 'LKFN', 'LKQX', 'LL', 'LLEN', 'LLL', 'LLNW', 'LLTC', 'LLY', 'LM', 'LMIA', 'LMNR', 'LMNX', 'LMT', 'LNC', 'LNCE', 'LNCR', 'LNDC', 'LNG', 'LNKD', 'LNN', 'LNT', 'LO', 'LOGM', 'LOOP', 'LOPE', 'LORL', 'LOW', 'LPLA', 'LPNT', 'LPS', 'LPSN', 'LPX', 'LQDT', 'LRCX', 'LRN', 'LRY', 'LSCC', 'LSE', 'LSI', 'LSTR', 'LSTZA', 'LTC', 'LTD', 'LTM', 'LTS', 'LTXC', 'LUB', 'LUFK', 'LUK', 'LUV', 'LVB', 'LVLT', 'LVS', 'LWAY', 'LWSN', 'LXK', 'LXP', 'LXRX', 'LXU', 'LYB', 'LYTS', 'LYV', 'LZ', 'LZB', 'M', 'MA', 'MAA', 'MAC', 'MAIN', 'MAKO', 'MAN', 'MANH', 'MANT', 'MAPP', 'MAR', 'MAS', 'MASI', 'MAT', 'MATW', 'MAXY', 'MBFI', 'MBI', 'MBLX', 'MBVT', 'MCC', 'MCD', 'MCF', 'MCGC', 'MCHP', 'MCHX', 'MCK', 'MCO', 'MCP', 'MCRI', 'MCRL', 'MCRS', 'MCS', 'MCY', 'MD', 'MDAS', 'MDC', 'MDCA', 'MDCI', 'MDCO', 'MDF', 'MDMD', 'MDP', 'MDR', 'MDRX', 'MDSO', 'MDT', 'MDTH', 'MDU', 'MDVN', 'MDW', 'MEA', 'MEAS', 'MED', 'MEDH', 'MEI', 'MENT', 'MERU', 'MET', 'METR', 'MF', 'MFA', 'MFB', 'MFLX', 'MFW', 'MG', 'MGAM', 'MGEE', 'MGI', 'MGLN', 'MGM', 'MGPI', 'MGRC', 'MHGC', 'MHK', 'MHLD', 'MHO', 'MHP', 'MHR', 'MHS', 'MI', 'MIDD', 'MIG', 'MILL', 'MIND', 'MINI', 'MIPS', 'MITI', 'MJN', 'MKC', 'MKL', 'MKSI', 'MKTG', 'MKTX', 'MLHR', 'MLI', 'MLM', 'MLNK', 'MLR', 'MMC', 'MMI', 'MMM', 'MMR', 'MMS', 'MMSI', 'MNI', 'MNKD', 'MNR', 'MNRO', 'MNTA', 'MO', 'MOD', 'MOG.A', 'MOH', 'MOLX', 'MON', 'MORN', 'MOS', 'MOSY', 'MOTR', 'MOV', 'MOVE', 'MPAA', 'MPG', 'MPR', 'MPW', 'MPWR', 'MPX', 'MRCY', 'MRGE', 'MRH', 'MRK', 'MRLN', 'MRO', 'MRTN', 'MRVL', 'MRX', 'MS', 'MSA', 'MSCC', 'MSCI', 'MSEX', 'MSFG', 'MSFT', 'MSG', 'MSI', 'MSL', 'MSM', 'MSO', 'MSPD', 'MSSR', 'MSTR', 'MSW', 'MTB', 'MTD', 'MTG', 'MTH', 'MTN', 'MTOR', 'MTOX', 'MTRN', 'MTRX', 'MTSC', 'MTW', 'MTX', 'MTZ', 'MU', 'MUR', 'MUSA', 'MVC', 'MVIS', 'MW', 'MWA', 'MWIV', 'MWV', 'MWW', 'MXIM', 'MXL', 'MXWL', 'MYE', 'MYGN', 'MYL', 'MYRG', 'N', 'NABI', 'NAFC', 'NANO', 'NARA', 'NAT', 'NATI', 'NATL', 'NATR', 'NAUH', 'NAV', 'NAVG', 'NBIX', 'NBL', 'NBR', 'NBS', 'NBTB', 'NC', 'NCI', 'NCIT', 'NCMI', 'NCR', 'NCS', 'NCT', 'NDAQ', 'NDN', 'NDSN', 'NEE', 'NEM', 'NEOG', 'NEOP', 'NETL', 'NEU', 'NEWP', 'NEWS', 'NFBK', 'NFG', 'NFLX', 'NFP', 'NFX', 'NGPC', 'NGS', 'NHC', 'NHI', 'NHP', 'NI', 'NICK', 'NIHD', 'NILE', 'NJR', 'NKE', 'NKSH', 'NKTR', 'NL', 'NLC', 'NLSN', 'NLY', 'NMFC', 'NMRX', 'NNBR', 'NNI', 'NNN', 'NOC', 'NOG', 'NOR', 'NOV', 'NP', 'NPBC', 'NPK', 'NPO', 'NPSP', 'NPTN', 'NR', 'NRCI', 'NRF', 'NRG', 'NSC', 'NSIT', 'NSM', 'NSP', 'NSR', 'NST', 'NSTC', 'NTAP', 'NTCT', 'NTGR', 'NTLS', 'NTRI', 'NTRS', 'NTSP', 'NU', 'NUAN', 'NUE', 'NUS', 'NUTR', 'NUVA', 'NVAX', 'NVDA', 'NVE', 'NVEC', 'NVLS', 'NVR', 'NVTL', 'NWBI', 'NWE', 'NWL', 'NWLI', 'NWN', 'NWPX', 'NWSA', 'NWY', 'NX', 'NXST', 'NXTM', 'NYB', 'NYMX', 'NYT', 'NYX', 'O', 'OABC', 'OAS', 'OB', 'OC', 'OCFC', 'OCLR', 'OCN', 'OCR', 'OCZ', 'ODC', 'ODFL', 'ODP', 'OEH', 'OFC', 'OFG', 'OFIX', 'OFLX', 'OGE', 'OGXI', 'OHI', 'OI', 'OII', 'OIS', 'OKE', 'OKSB', 'OLN', 'OLP', 'OMC', 'OMCL', 'OME', 'OMEX', 'OMG', 'OMI', 'OMN', 'OMPI', 'OMX', 'ONB', 'ONE', 'ONNN', 'ONTY', 'ONXX', 'OPEN', 'OPK', 'OPLK', 'OPNT', 'OPTR', 'OPWV', 'OPXT', 'OPY', 'ORA', 'ORB', 'ORBC', 'ORCL', 'OREX', 'ORI', 'ORIT', 'ORLY', 'ORN', 'ORRF', 'OSG', 'OSIR', 'OSIS', 'OSK', 'OSTK', 'OSUR', 'OTTR', 'OUTD', 'OVTI', 'OWW', 'OXM', 'OXPS', 'OXY', 'OYOG', 'OZRK', 'PACB', 'PACR', 'PACW', 'PAET', 'PAG', 'PANL', 'PATR', 'PAY', 'PAYX', 'PBCT', 'PBH', 'PBI', 'PBNY', 'PBY', 'PCAR', 'PCBC', 'PCBK', 'PCCC', 'PCG', 'PCH', 'PCL', 'PCLN', 'PCP', 'PCRX', 'PCS', 'PCX', 'PCYC', 'PDC', 'PDCO', 'PDFS', 'PDLI', 'PDM', 'PEB', 'PEBO', 'PEET', 'PEG', 'PEGA', 'PEI', 'PENN', 'PEP', 'PERY', 'PETD', 'PETM', 'PETS', 'PFCB', 'PFE', 'PFG', 'PFS', 'PG', 'PGI', 'PGN', 'PGNX', 'PGR', 'PH', 'PHH', 'PHIIK', 'PHM', 'PHX', 'PICO', 'PII', 'PIKE', 'PIP', 'PIR', 'PJC', 'PKD', 'PKE', 'PKG', 'PKI', 'PKOH', 'PKT', 'PKY', 'PL', 'PLAB', 'PLCE', 'PLCM', 'PLD', 'PLFE', 'PLL', 'PLOW', 'PLPC', 'PLT', 'PLUS', 'PLXS', 'PLXT', 'PM', 'PMC', 'PMCS', 'PMFG', 'PMI', 'PMT', 'PMTC', 'PMTI', 'PNC', 'PNFP', 'PNK', 'PNM', 'PNNT', 'PNNW', 'PNR', 'PNRA', 'PNW', 'PNX', 'PNY', 'PODD', 'POL', 'POM', 'POOL', 'POR', 'POWI', 'POWL', 'POWR', 'POZN', 'PPC', 'PPD', 'PPDI', 'PPG', 'PPHM', 'PPL', 'PPO', 'PPS', 'PQ', 'PRA', 'PRAA', 'PRE', 'PRFT', 'PRGO', 'PRGS', 'PRGX', 'PRI', 'PRIM', 'PRK', 'PRM', 'PRMW', 'PRO', 'PROJ', 'PRS', 'PRSC', 'PRSP', 'PRTS', 'PRU', 'PRX', 'PRXL', 'PSA', 'PSB', 'PSEC', 'PSEM', 'PSMT', 'PSS', 'PSSI', 'PSTB', 'PSUN', 'PTEN', 'PTIE', 'PTP', 'PTRY', 'PTX', 'PULS', 'PVA', 'PVH', 'PVTB', 'PWAV', 'PWER', 'PWOD', 'PWR', 'PX', 'PXD', 'PXP', 'PZG', 'PZN', 'PZZA', 'QADA', 'QCOM', 'QCOR', 'QDEL', 'QEP', 'QGEN', 'QLGC', 'QLIK', 'QLTY', 'QNST', 'QPSA', 'QSFT', 'QSII', 'QTM', 'QUAD', 'R', 'RA', 'RAD', 'RADS', 'RAH', 'RAI', 'RAIL', 'RAS', 'RAVN', 'RAX', 'RBC', 'RBCAA', 'RBCN', 'RBN', 'RCII', 'RCKB', 'RCL', 'RDC', 'RDEA', 'RDEN', 'RDK', 'RDN', 'RDNT', 'RE', 'RECN', 'REG', 'REGN', 'RELL', 'REN', 'RENT', 'RES', 'REV', 'REX', 'REXX', 'RF', 'RFMD', 'RGA', 'RGC', 'RGLD', 'RGR', 'RGS', 'RHI', 'RHT', 'RIGL', 'RIMG', 'RJET', 'RJF', 'RKT', 'RL', 'RLD', 'RLH', 'RLI', 'RLJ', 'RLOC', 'RLRN', 'RMBS', 'RMD', 'RMTI', 'RNET', 'RNOW', 'RNR', 'RNST', 'RNWK', 'ROC', 'ROCK', 'ROG', 'ROIC', 'ROK', 'ROL', 'ROLL', 'ROMA', 'ROP', 'ROSE', 'ROST', 'ROVI', 'RP', 'RPM', 'RPT', 'RPTP', 'RPXC', 'RRC', 'RRD', 'RRGB', 'RRR', 'RRTS', 'RS', 'RSG', 'RSH', 'RSO', 'RST', 'RSTI', 'RSYS', 'RT', 'RTEC', 'RTI', 'RTIX', 'RTK', 'RTN', 'RUE', 'RURL', 'RUSHA', 'RUTH', 'RVBD', 'RVM', 'RWT', 'RYL', 'RYN', 'S', 'SAAS', 'SABA', 'SAFM', 'SAFT', 'SAH', 'SAI', 'SAIA', 'SAM', 'SANM', 'SAPE', 'SASR', 'SATC', 'SATS', 'SAVE', 'SBAC', 'SBCF', 'SBGI', 'SBH', 'SBIB', 'SBNY', 'SBRA', 'SBSI', 'SBUX', 'SBX', 'SCBT', 'SCCO', 'SCG', 'SCHL', 'SCHN', 'SCHS', 'SCHW', 'SCI', 'SCL', 'SCLN', 'SCMP', 'SCMR', 'SCOR', 'SCS', 'SCSC', 'SCSS', 'SCVL', 'SD', 'SE', 'SEAC', 'SEB', 'SEE', 'SEH', 'SEIC', 'SEM', 'SEMG', 'SENEA', 'SF', 'SFD', 'SFE', 'SFG', 'SFI', 'SFL', 'SFLY', 'SFN', 'SFNC', 'SFSF', 'SFY', 'SGA', 'SGEN', 'SGI', 'SGK', 'SGMO', 'SGMS', 'SGNT', 'SGS', 'SGY', 'SHAW', 'SHEN', 'SHFL', 'SHLD', 'SHLM', 'SHLO', 'SHO', 'SHOO', 'SHOR', 'SHS', 'SHW', 'SIAL', 'SIG', 'SIGA', 'SIGI', 'SIGM', 'SIMG', 'SIRI', 'SIRO', 'SIVB', 'SIX', 'SJI', 'SJM', 'SJW', 'SKH', 'SKS', 'SKT', 'SKX', 'SKY', 'SKYW', 'SLAB', 'SLB', 'SLE', 'SLG', 'SLGN', 'SLH', 'SLM', 'SLRC', 'SLTM', 'SLXP', 'SM', 'SMA', 'SMBL', 'SMCI', 'SMG', 'SMOD', 'SMP', 'SMRT', 'SMSC', 'SMSI', 'SMTC', 'SNA', 'SNBC', 'SNCR', 'SNDK', 'SNH', 'SNHY', 'SNI', 'SNMX', 'SNPS', 'SNSS', 'SNTA', 'SNTS', 'SNV', 'SNX', 'SO', 'SOA', 'SOLR', 'SON', 'SONC', 'SONE', 'SONO', 'SONS', 'SPAR', 'SPB', 'SPF', 'SPG', 'SPLS', 'SPN', 'SPNC', 'SPPI', 'SPR', 'SPRT', 'SPSC', 'SPTN', 'SPW', 'SPWRA', 'SQI', 'SQNM', 'SRCE', 'SRCL', 'SRDX', 'SRE', 'SREV', 'SRI', 'SRSL', 'SRX', 'SRZ', 'SSD', 'SSI', 'SSNC', 'SSP', 'SSS', 'SSYS', 'STAA', 'STAG', 'STAN', 'STBA', 'STBC', 'STBZ', 'STC', 'STE', 'STEC', 'STEI', 'STEL', 'STFC', 'STI', 'STJ', 'STL', 'STLD', 'STMP', 'STNG', 'STNR', 'STR', 'STRA', 'STRI', 'STRL', 'STSA', 'STT', 'STWD', 'STXS', 'STZ', 'SUBK', 'SUG', 'SUI', 'SUMR', 'SUN', 'SUNH', 'SUNS', 'SUP', 'SUPG', 'SUPX', 'SURG', 'SURW', 'SUSQ', 'SUSS', 'SVNT', 'SVU', 'SVVS', 'SWC', 'SWFT', 'SWHC', 'SWI', 'SWK', 'SWKS', 'SWM', 'SWN', 'SWS', 'SWSH', 'SWX', 'SWY', 'SXCI', 'SXI', 'SXT', 'SYA', 'SYBT', 'SYK', 'SYKE', 'SYMC', 'SYMM', 'SYMS', 'SYNA', 'SYNM', 'SYNO', 'SYNT', 'SYUT', 'SYX', 'SYY', 'SZYM', 'T', 'TAL', 'TAP', 'TASR', 'TAST', 'TAXI', 'TAYC', 'TBBK', 'TBI', 'TBL', 'TBNK', 'TC', 'TCAP', 'TCB', 'TCBI', 'TCBK', 'TCO', 'TCRD', 'TDC', 'TDG', 'TDS', 'TDW', 'TDY', 'TE', 'TECD', 'TECH', 'TECUA', 'TEG', 'TEN', 'TER', 'TESO', 'TEX', 'TFM', 'TFSL', 'TFX', 'TG', 'TGH', 'TGI', 'TGT', 'THC', 'THFF', 'THG', 'THO', 'THOR', 'THQI', 'THR', 'THRX', 'THS', 'TIBX', 'TICC', 'TIE', 'TIF', 'TIN', 'TINY', 'TISI', 'TITN', 'TIVO', 'TJX', 'TK', 'TKLC', 'TKR', 'TLAB', 'TLB', 'TLEO', 'TMH', 'TMK', 'TMO', 'TMP', 'TMS', 'TNAV', 'TNB', 'TNC', 'TNDM', 'TNK', 'TNS', 'TOBC', 'TOL', 'TOWN', 'TOWR', 'TPC', 'TPCG', 'TPLM', 'TPX', 'TQNT', 'TR', 'TRAK', 'TRC', 'TRCR', 'TREX', 'TRGP', 'TRGT', 'TRH', 'TRI', 'TRK', 'TRLG', 'TRMB', 'TRMK', 'TRN', 'TRNO', 'TRNX', 'TROW', 'TRR', 'TRS', 'TRST', 'TRV', 'TRW', 'TSCO', 'TSLA', 'TSN', 'TSO', 'TSPT', 'TSRA', 'TSRX', 'TSS', 'TSYS', 'TTC', 'TTEC', 'TTEK', 'TTGT', 'TTI', 'TTMI', 'TTWO', 'TUC', 'TUES', 'TUP', 'TVL', 'TW', 'TWC', 'TWER', 'TWGP', 'TWI', 'TWIN', 'TWO', 'TWTC', 'TWX', 'TXI', 'TXN', 'TXRH', 'TXT', 'TYC', 'TYL', 'TYPE', 'TZOO', 'UA', 'UACL', 'UAL', 'UAM', 'UBA', 'UBNK', 'UBSH', 'UBSI', 'UCBID', 'UCTT', 'UDR', 'UDRL', 'UEC', 'UEIC', 'UFCS', 'UFI', 'UFPI', 'UFS', 'UGI', 'UHAL', 'UHS', 'UHT', 'UIL', 'UIS', 'ULTA', 'ULTI', 'ULTR', 'UMBF', 'UMH', 'UMPQ', 'UNF', 'UNFI', 'UNH', 'UNIS', 'UNM', 'UNP', 'UNS', 'UNT', 'UNTD', 'UNTK', 'UPI', 'UPL', 'UPS', 'URBN', 'URG', 'URI', 'URRE', 'URS', 'URZ', 'USAP', 'USB', 'USEG', 'USG', 'USLM', 'USM', 'USMO', 'USNA', 'USPH', 'USTR', 'USU', 'UTEK', 'UTHR', 'UTI', 'UTIW', 'UTL', 'UTR', 'UTX', 'UVE', 'UVSP', 'UVV', 'UXG', 'V', 'VAL', 'VALU', 'VAR', 'VASC', 'VC', 'VCBI', 'VCI', 'VCLK', 'VDSI', 'VECO', 'VFC', 'VG', 'VGR', 'VGZ', 'VHC', 'VIA.B', 'VIAS', 'VICL', 'VICR', 'VITA', 'VIVO', 'VLCCF', 'VLGEA', 'VLNC', 'VLO', 'VLTR', 'VLY', 'VMC', 'VMED', 'VMI', 'VMW', 'VNDA', 'VNO', 'VOCS', 'VOG', 'VOLC', 'VOXX', 'VPFG', 'VPG', 'VPHM', 'VPRT', 'VQ', 'VR', 'VRA', 'VRNT', 'VRS', 'VRSK', 'VRSN', 'VRTS', 'VRTU', 'VRTX', 'VRUS', 'VSAT', 'VSEA', 'VSEC', 'VSH', 'VSI', 'VTG', 'VTR', 'VVC', 'VVI', 'VVTV', 'VVUS', 'VZ', 'WAB', 'WABC', 'WAC', 'WAG', 'WAL', 'WASH', 'WAT', 'WAVX', 'WBC', 'WBCO', 'WBMD', 'WBS', 'WBSN', 'WCAA', 'WCBO', 'WCC', 'WCG', 'WCN', 'WCRX', 'WD', 'WDC', 'WDFC', 'WDR', 'WEC', 'WEN', 'WERN', 'WEYS', 'WFC', 'WFD', 'WFM', 'WFR', 'WFSL', 'WG', 'WGL', 'WGO', 'WHG', 'WHR', 'WIBC', 'WIFI', 'WIN', 'WINA', 'WINN', 'WIRE', 'WLB', 'WLK', 'WLL', 'WLP', 'WLT', 'WM', 'WMAR', 'WMB', 'WMG', 'WMGI', 'WMK', 'WMS', 'WMT', 'WNC', 'WNI', 'WNR', 'WOOF', 'WOR', 'WPI', 'WPO', 'WPP', 'WR', 'WRB', 'WRC', 'WRE', 'WRES', 'WRI', 'WRLD', 'WSBC', 'WSC', 'WSFS', 'WSM', 'WSO', 'WSR', 'WST', 'WSTL', 'WTBA', 'WTFC', 'WTI', 'WTM', 'WTR', 'WTS', 'WTSLA', 'WTW', 'WU', 'WWD', 'WWE', 'WWON', 'WWW', 'WWWW', 'WXS', 'WY', 'WYN', 'WYNN', 'X', 'XCO', 'XEC', 'XEL', 'XIDE', 'XL', 'XLNX', 'XNPT', 'XOM', 'XRAY', 'XRIT', 'XRM', 'XRTX', 'XRX', 'XTXI', 'XXIA', 'Y', 'YDNT', 'YHOO', 'YORW', 'YSI', 'YUM', 'ZAGG', 'ZBRA', 'ZEP', 'ZEUS', 'ZGNX', 'ZIGO', 'ZINC', 'ZION', 'ZIOP', 'ZIP', 'ZIXI', 'ZLC', 'ZLCS', 'ZMH', 'ZN', 'ZOLL', 'ZOLT', 'ZQK', 'ZRAN', 'ZUMZ', 'ZZ']