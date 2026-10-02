---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: DEUTSCHE BANK - MANUAL OTC
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: DEUTSCHE BANK AG MARKET SEGMENT MARKET CODE FOR MANUAL OTC FILLS AS PER MMT2 STANDARD DEFINITION PROPOSED BY FIXPROTOCOL.ORG
      AND SUPPORTED BY EUROPEAN TDM'S(HTTP://WWW.BATSTRADING.CO.UK/BXTR/)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: MANUAL OTC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: DEUTSCHE BANK - MANUAL OTC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://autobahn.db.com/microsite/html/equity.html
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBAG.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBAG
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-7LTWFZYICNSX8D621K86.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-7LTWFZYICNSX8D621K86
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBMO
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: DEUTSCHE BANK - MANUAL OTC
type: Ontology Individual
---

# DEUTSCHE BANK - MANUAL OTC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBMO>

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Frankfurt](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md)
- **Related to**: [Facility-DBAG](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBAG.md)
- **Related to**: [ServiceProvider-L-7LTWFZYICNSX8D621K86](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-7LTWFZYICNSX8D621K86.md)

## Annotations

- **label**: DEUTSCHE BANK - MANUAL OTC
- **note**: DEUTSCHE BANK AG MARKET SEGMENT MARKET CODE FOR MANUAL OTC FILLS AS PER MMT2 STANDARD DEFINITION PROPOSED BY FIXPROTOCOL.ORG AND SUPPORTED BY EUROPEAN TDM'S(HTTP://WWW.BATSTRADING.CO.UK/BXTR/)
- **hasFacilityAcronym**: MANUAL OTC
- **hasFormalName**: DEUTSCHE BANK - MANUAL OTC
- **hasWebsite**: https://autobahn.db.com/microsite/html/equity.html

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
