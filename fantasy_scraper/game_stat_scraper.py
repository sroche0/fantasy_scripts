__author__ = 'sroche'
import requests
from bs4 import BeautifulSoup

#
# def get_site_info(url):
#     r = requests.get(url)

cookies = {
    'signInLayout': '%7B%22signInSite%22%3A%22quadrant-1%22%2C%22signInSocial%22%3A%22quadrant-2%22%2C%22register%22%3A%22quadrant-3%22%2C%22registerBenefits%22%3A%22quadrant-4%22%7D',
    'mbox': 'session#1437506215223-51357#1437510847|PC#1437506215223-51357.28_13#1438718587|check#true#1437509047',
    's_sess': '%20s_cc%3Dtrue%3B%20s_ppv%3D-%252C100%252C100%252C540%3B%20s_sq%3Dnflmultiplatform%253D%252526pid%25253Dnfl%2525253Areg%2525253Aprofile%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fid2.s.nfl.com%2525252Ffans%2525252Flogin%2525253FreturnTo%2525253Dhttp%252525253A%252525252F%252525252Fwww.nfl.com%252525252Ffans%252525252Fprofile%252525252Fsroche0_1%252526oidt%25253D1%252526ot%25253DA%252526oi%25253D1%3B',
    's_pers': '%20s_lastvisit%3D1437508054971%7C1532116054971%3B%20s_fid%3D2CF9BE5C6B684C1B-140B1DAF90D7C8AB%7C1500667385773%3B%20s_nr%3D1437508992549%7C1440100992549%3B%20s_pv%3Dnfl%253Areg%253Alogin%7C1437510792550%3B%20p36%3Dsroche0%257Cfire%7C1595188992551%3B',
    's_vi': '[CS]v1|2AD74D4D8501019D-60000104200B46F2[CE]',
    '__psrw': 'dfd9919d-7604-4d11-8b09-d0c45638c78e',
    '__tuuid': 'dfd9919d-7604-4d11-8b09-d0c45638c78e',
    'JSESSIONID': '6194F517CD610C1E4818E87CCDC82C25',
    'aamnfl': 'fantasy%3D01%3Bepfavteam%3Djets%3Bemg%3Dfppft%3Bemg%3Dfpplof%3Bemg%3Dfppkm%3Bemg%3Dfptnf%3BFanPly14%3DFanPly14%3Bpclvty%3DFYMngAcq%3Bpclvty%3DFYPubAcq%3Bpclvty%3DGRAcq%3Bpclvty%3DGPAcq%3Bpclvtytickets%3DPatriots%3Bkidsjerseys%3Dacq%3Bmensheadwear%3Dacq%3Bmensjerseys%3Dacq%3Bwomensjerseys%3Dacq%3Bfan14%3Dnopickem%3Bnflnoweps%3Dregistered%3BFanPly15%3DFanPly15%3BEpsilon%3DRegisteredNonGP',
    'aam_sc': 'aamsc%3D513545%7C596146%7C1886561',
    'aam_did': '78187065377271497570416052539262920016',
    'ARSL': '3v4sSD3TpmmL-bufuGaZl5mSw58gLqWn6gLzE3G43IXDtWf8d13KTHA',
    '__gads': 'ID=5fec0dcbfbd132e3:T=1437506279:S=ALNI_Mb65Z0DCV_J3UE8EkbqD2gEpBTRCw',
    'navigationTeamsDDOpen': 'true',
    'headerSubProducts': 'preseasonLiveClass%2CgameRewindClass',
    'fsr.s': '%7B%22v2%22%3A-2%2C%22v1%22%3A1%2C%22rid%22%3A%22dd8f309-61816814-42a3-35ff-7e211%22%2C%22to%22%3A5%2C%22c%22%3A%22http%3A%2F%2Fwww.nfl.com%2Ffans%2Fprofile%2Fsroche0%22%2C%22pv%22%3A4%2C%22lc%22%3A%7B%22d1%22%3A%7B%22v%22%3A4%2C%22s%22%3Atrue%7D%7D%2C%22cd%22%3A1%2C%22f%22%3A1437508973764%2C%22sd%22%3A1%2C%22l%22%3A%22en%22%2C%22i%22%3A-1%7D',
    '_cb_ls': '1',
    '_chartbeat2': 'DxKCwUBGCytDBLC2Ic.1437508847560.1437508987500.1',
    'glt_2_kMCvXUlFCZJhwaNXbxzePaXPYb9T__rgiF5y7EnWuEM5a84cueVv-MkPRKjVFc31': 'LT3_fF07v-F3B18wVoJxccCRv8WLXN8it3eLRJZNXnS9lhs%7CUUID%3D3a322a0e39644de6a6bc9af49f642140',
    'fsr.r': '%7B%22d%22%3A90%2C%22i%22%3A%22dd8f309-61816814-42a3-35ff-7e211%22%2C%22e%22%3A1438113782830%7D',
}

headers = {
    'Host': 'id2.s.nfl.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://id2.s.nfl.com/fans/login?returnTo=http%3A%2F%2Fwww.nfl.com%2Ffans%2Fprofile%2Fsroche0',
    'Connection': 'keep-alive',
}

data = 'username=sroche0&password=0vuWLLHz&cookiePersisted=on&successUrl=&s=&modal=1'

r = requests.post('https://id2.s.nfl.com/fans/login?returnTo=http%3A%2F%2Fwww.nfl.com%2Ffans%2Fprofile%2Fsroche0', headers=headers, cookies=cookies, data=data)

print r.text