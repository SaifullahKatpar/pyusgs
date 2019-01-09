# this module hadnles and routes the requests to appropriate USGS web service

# dictionary of all base urls

base_urls = {
     "site":"https://wwww.waterservices.usgs.gov/nwis/site/",
     "quality": "https://wwww.waterservices.usgs.gov/nwis/",
     "daily-values":"//waterservices.usgs.gov/nwis/dv/",
     "ground-water":"https://wwww.waterservices.usgs.gov/nwis/gwlevels/",
     "statistics":"https://wwww.waterservices.usgs.gov/nwis/stat/"
     }
codes = {
          "state":['al','ak','az','ar','ca','co','ct','de','fl','ga','hi','id','il','in','ia','ks','ky','la','me','md','ma','mi','mn','ms','mo','mt','ne','nv','nh','nj','nm','ny','nc','nd','oh','ok','or','pa','ri','sc','sd','tn','tx','ut','vt','va','wa','wv','wi','wy'],

          }
