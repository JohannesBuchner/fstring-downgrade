if outdir=='': outdir = f'./PipeV{Version:d}{VersApp:s}_results'
BoxCat2 = os.path.join(outdir, f"{outprefix}020_BoxCa2.fits")
if 1:
        cmd_evtool.append(["evtool",
        f"eventfiles={infile}",
        f"outfile={os.path.join(outdir,'EvtImg_full.fits')}",
        f"emin=0",
        f"emax=100",
        f"image=yes",
        f"rebin=80",
        f"size=18000 9000",
        f"pattern=15",
        f"center_position=0 0"
        ])
        logfile = os.path.join(outdir, f'eFEDS_V{Version:03d}{VersApp}.par')

EvtImgFiles = [os.path.join(outdir, f"{outprefix}02{bname}_EvtImg.fits") for bname in bandname]
        "emin=" + " ".join(f"{x:g}" for x in emin_keV)

cmd_erbox2 = ["erbox",
        f"images={' '.join(EvtImgFiles)}",
        f"boxlist={BoxCat2}",
        f"expimages={' '.join(ExpMapFiles)}",
        f"detmasks={DetMask}",
        f"bkgimages={' '.join(BkgMapFiles)}",
        f"emin=" + " ".join(f"{x*1000:g}" for x in emin_keV),
        f"emax=" + " ".join(f"{x*1000:g}" for x in emax_keV),
        f"hrdef=",
        f"ecf=" + " ".join(f"{x:g}" for x in ecf),
        f"nruns=2",
        ]
