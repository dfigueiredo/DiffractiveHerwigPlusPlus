import FWCore.ParameterSet.Config as cms

process = cms.Process('Analysis')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring("file:../Herwig_Diffractive_UE_7TeV_cff_py_GEN.root")
)

#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
#process.load('PhysicsTools.HepMCCandAlgos.genParticles_cfi')
#process.load('RecoJets.Configuration.GenJetParticles_cff')
#process.load('RecoJets.Configuration.RecoGenJets_cff')

#process.genParticles.abortOnUnknownPDGCode = False

process.genParticlesVisible = cms.EDFilter("GenJetParticleRefSelector",
    includeList = cms.vstring(),
    src = cms.InputTag("genParticles"),
    stableOnly = cms.bool(True),
    verbose = cms.untracked.bool(True),
    excludeList = cms.vstring('nu_e', 
        'nu_mu', 
        'nu_tau', 
        'mu-', 
        '~chi_10', 
        '~nu_eR', 
        '~nu_muR', 
        '~nu_tauR', 
        'Graviton', 
        '~Gravitino', 
        'nu_Re', 
        'nu_Rmu', 
        'nu_Rtau', 
        'nu*_e0', 
        'Graviton*')
)

process.SDDijets = cms.EDAnalyzer("SDDijetsAnalyzer",
	GenParticleTag = cms.InputTag("genParticles"),
	GenJetTag = cms.InputTag("ak5GenJets"),
        EBeam = cms.double(3500.0),
	debug = cms.untracked.bool(True)
)

process.add_(cms.Service("TFileService",
		fileName = cms.string("analysisDiffractionUE_histos.root")
	)
)

process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
                                   src = cms.InputTag("genParticles"),
                                   printP4 = cms.untracked.bool(False),
                                   printPtEtaPhi = cms.untracked.bool(False),
                                   printVertex = cms.untracked.bool(False),
                                   printStatus = cms.untracked.bool(False),
                                   printIndex = cms.untracked.bool(False),
                                   status = cms.untracked.vint32( 3 )
                                   )

process.analysis = cms.Path(process.genParticlesVisible*process.SDDijets)
