# Years
CEN_YEARS = [
    1951, 1956, 1961, 1966, 1971, 1976, 1981, 1986, 1991, 1996, 
    2001, 2006, 2011, 2016, 2021
]

FED_YEARS = [1952, 1966, 1976, 1987, 1996, 1999, 2003, 2013, 2022]
ONTED_YEARS = [1962, 1966, 1975, 1987, 1996, 2005, 2015]

FELXN_YEARS = [
    1962, 1963, 1965, 1968, 1972, 1974, 1979, 1980, 1984, 1988, 
    1993, 1997, 2000, 2004, 2006, 2008, 2011, 2015, 2019, 2021,
    2025,
]
ONTELXN_YEARS = [
    1963, 1967, 1971, 1975, 1977, 1981, 1985, 1987, 1990, 1995, 
    1999, 2003, 2007, 2011, 2014, 2018, 2022, 2025
]

# Census variables
YEAR_CODES = {
    1951: {
        'num_pop_tot': ['pop__tot1951ttd'],
        'num_imm_tot': [],
        'num_imm_new': [],
        'num_imm_2nd_tot': [],
        'avg_hou_inc': [],
        'num_not_vm_tot': [],
        'num_vm_sa_tot': [],
        'num_vm_chn_tot': [],
        'num_enfr_home_tot': [],
    }, 
    1956: {
        'num_pop_tot': ['pop__tot1956ttd'],
        'num_imm_tot': [],
        'num_imm_new': [],
        'num_imm_2nd_tot': [],
        'avg_hou_inc': [],
        'num_not_vm_tot': [],
        'num_vm_sa_tot': [],
        'num_vm_chn_tot': [],
        'num_enfr_home_tot': [],
    }, 
    1961: {
        'num_pop_tot': ['pop__tot1961ttd'],
        'num_imm_tot': ['imb__tot1961ttd'],
        'num_imm_new': ['impi19611961tt1', 'impi19601961tt1', 'impi195819591961tt1', 'impi195619571961tt1'],  # , 'impi195119551961tt1'
        'num_imm_2nd_tot': [],
        'avg_hou_inc': [],
        'num_not_vm_tot': [],
        'num_vm_sa_tot': [],
        'num_vm_chn_tot': [],
        'num_enfr_home_tot': [],
    }, 
    1966: {
        'num_pop_tot': ['pop__tot1966ttd'],
        'num_imm_tot': [],
        'num_imm_new': [],
        'num_imm_2nd_tot': [],
        'avg_hou_inc': [],
        'num_not_vm_tot': [],
        'num_vm_sa_tot': [],
        'num_vm_chn_tot': [],
        'num_enfr_home_tot': [],
    }, 
    1971: {
        'num_pop_tot': ['pop__tot1971ttd'],
        'num_imm_tot': ['imb__tot1971ttd'],
        'num_imm_new': [],
        'num_imm_2nd_tot': [],
        'avg_hou_inc': ['ihat_avg1971ttn'],
        'num_not_vm_tot': [],
        'num_vm_sa_tot': [],
        'num_vm_chn_tot': [],
        'num_enfr_home_tot': ['lnh_1resoffien__1971tt1', 'lnh_1resoffifr__1971tt1'],
    }, 
    1976: {
        'num_pop_tot': ['pop__tot1976ttd'],
        'num_imm_tot': [],
        'num_imm_new': [],
        'num_imm_2nd_tot': [],
        'avg_hou_inc': [],
        'num_not_vm_tot': [],
        'num_vm_sa_tot': [],
        'num_vm_chn_tot': [],
        'num_enfr_home_tot': [],
    }, 
    1981: {
        'num_pop_tot': ['pop__tot1981ttd'],
        'num_imm_tot': ['impi_tot1981ttd'],  # impi_tot1981ttd (CSD + CT) or imag_tot1981ttd (CT), the usual is broken
        'num_imm_new': ['impi197819811981tt1'],  # 'impi197019771981tt1'
        'num_imm_2nd_tot': [],
        'avg_hou_inc': ['ihat_avg1981ttn'],
        'num_not_vm_tot': [],
        'num_vm_sa_tot': [],
        'num_vm_chn_tot': [],
        'num_enfr_home_tot': ['lnh_1resoffien__1981tt1', 'lnh_1resoffifr__1981tt1'],
    }, 
    1986: {
        'num_pop_tot': ['pop__tot1986ttd'],
        'num_imm_tot': ['imb__tot1986ttd'],
        'num_imm_new': ['impi198319861986tt1'],  # 'impi197819821986tt1'
        'num_imm_2nd_tot': [],
        'avg_hou_inc': ['ihat_avg1986ttn'],
        'num_not_vm_tot': [],
        'num_vm_sa_tot': [],
        'num_vm_chn_tot': [],
        'num_enfr_home_tot': ['lnh_1resoffien__1986tt1', 'lnh_1resoffifr__1986tt1'],
    }, 
    1991: {
        'num_pop_tot': ['pop__tot1991ttd'],
        'num_imm_tot': ['imd__tot1991ttd'],
        'num_imm_new': ['impi198819911991tt1'],  # 'impi198119871991tt1'
        'num_imm_2nd_tot': [],
        'avg_hou_inc': ['ihat_avg1991ttn'],
        'num_not_vm_tot': [],
        'num_vm_sa_tot': [],
        'num_vm_chn_tot': [],
        'num_enfr_home_tot': ['lnh_1resoffien__1991tt1', 'lnh_1resoffifr__1991tt1'],
    }, 
    1996: {
        'num_pop_tot': ['pop__tot1996ttd'],
        'num_imm_tot': ['imb__tot1996ttd'],
        'num_imm_new': ['impi199119961996tt1'],  # 'impi198119901996tt1'
        'num_imm_2nd_tot': [],
        'avg_hou_inc': ['ihat_avg1996ttn'],
        'num_not_vm_tot': ['vminnvis1996tt1'],
        'num_vm_sa_tot': ['vminvisisasi1996tt1'],
        'num_vm_chn_tot': ['vminvisichin1996tt1'],
        'num_enfr_home_tot': ['lnh_1resoffien__1996tt1', 'lnh_1resoffifr__1996tt1', 'lnh_mresenfr1996tt1'],
    }, 
    2001: {
        'num_pop_tot': ['pop__tot2001ttd'],
        'num_imm_tot': ['imb__tot2001ttd'],
        'num_imm_new': ['impi199620012001tt1'],  # 'impi199119952001tt1'
        'num_imm_2nd_tot': ['imgsgen22001tt1'],
        'avg_hou_inc': ['ihat_avg2001ttn'],
        'num_not_vm_tot': ['vminnvis2001tt1'],
        'num_vm_sa_tot': ['vminvisisasi2001tt1'],
        'num_vm_chn_tot': ['vminvisichin2001tt1'],
        'num_enfr_home_tot': ['lnh_1resoffien__2001tt1', 'lnh_1resoffifr__2001tt1', 'lnh_mresenfr2001tt1'],
    }, 
    2006: {
        'num_pop_tot': ['pop__tot2006ttd'],
        'num_imm_tot': ['imb__tot2006ttd'],
        'num_imm_new': ['impi200120062006tt1'],  # 'impi199620002006tt1'
        'num_imm_2nd_tot': ['imgsgen22006tt1'],
        'avg_hou_inc': ['ihat_avg2006ttn'],
        'num_not_vm_tot': ['vminnvis2006tt1'],
        'num_vm_sa_tot': ['vminvisisasi2006tt1'],
        'num_vm_chn_tot': ['vminvisichin2006tt1'],
        'num_enfr_home_tot': ['lnh_1resoffien__2006tt1', 'lnh_1resoffifr__2006tt1', 'lnh_mresenfr2006tt1'],
    }, 
    2011: {
        'num_pop_tot': ['pop__tot2011ttd'],
        'num_imm_tot': ['imb__tot2011ttd'],
        'num_imm_new': ['impi200620112011tt1'],  # 'impi200120052011tt1'
        'num_imm_2nd_tot': ['imgsgen22011tt1'],
        'avg_hou_inc': ['ihat_avg2011ttn'],
        'num_not_vm_tot': ['vminnvis2011tt1'],
        'num_vm_sa_tot': ['vminvisisasi2011tt1'],
        'num_vm_chn_tot': ['vminvisichin2011tt1'],
        'num_enfr_home_tot': ['lnh_1resoffien__2011tt1', 'lnh_1resoffifr__2011tt1', 'lnh_mresenfr2011tt1'],
    }, 
    2016: {
        'num_pop_tot': ['pop__tot2016ttd'],
        'num_imm_tot': ['imb__tot2016ttd'],
        'num_imm_new': ['impi201120162016tt1'],  # 'impi200620102016tt1'
        'num_imm_2nd_tot': ['imgsgen22016tt1'],
        'avg_hou_inc': ['ihat_avg2016ttn'],
        'num_not_vm_tot': ['vminnvis2016tt1'],
        'num_vm_sa_tot': ['vminvisisasi2016tt1'],
        'num_vm_chn_tot': ['vminvisichin2016tt1'],
        'num_enfr_home_tot': ['lnh_1resoffien__2016tt1', 'lnh_1resoffifr__2016tt1', 'lnh_mresenfr2016tt1'],
    }, 
    2021: {
        'num_pop_tot': ['pop__tot2021ttd'],
        'num_imm_tot': ['imb__tot2021ttd'],
        'num_imm_new': ['impi201620212021tt1'],  # 'impi201120152021tt1'
        'num_imm_2nd_tot': ['imgsgen22021tt1'],
        'avg_hou_inc': ['ihat_avg2021ttn'],
        'num_not_vm_tot': ['vminnvis2021tt1'],
        'num_vm_sa_tot': ['vminvisisasi2021tt1'],
        'num_vm_chn_tot': ['vminvisichin2021tt1'],
        'num_enfr_home_tot': ['lnh_1resoffien__2021tt1', 'lnh_1resoffifr__2021tt1', 'lnh_mresenfr2021tt1'],
    },
}