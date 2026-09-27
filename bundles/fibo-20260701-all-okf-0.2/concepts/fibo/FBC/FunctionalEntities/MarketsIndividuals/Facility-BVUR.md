---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BOLSA ELECTRONICA DE VALORES DEL URUGUAY
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGISTERED ELECTRONIC STOCK EXCHANGE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BOLSA ELECTRONICA DE VALORES DEL URUGUAY
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://web.bevsa.com.uy/bevsaintranet2008/inicio/default.aspx
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Montevideo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Montevideo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSAELECTRONICADEVALORESDELURUGUAY.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSAELECTRONICADEVALORESDELURUGUAY
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Uruguay
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BVUR
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BOLSA ELECTRONICA DE VALORES DEL URUGUAY
type: Ontology Individual
---

# BOLSA ELECTRONICA DE VALORES DEL URUGUAY

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BVUR>

## Relationships

- **Related to**: [Uruguay](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Uruguay>)
- **Related to**: [Montevideo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Montevideo.md)
- **Related to**: [ServiceProvider-BOLSAELECTRONICADEVALORESDELURUGUAY](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSAELECTRONICADEVALORESDELURUGUAY.md)

## Annotations

- **label**: BOLSA ELECTRONICA DE VALORES DEL URUGUAY
- **note**: REGISTERED ELECTRONIC STOCK EXCHANGE.
- **hasFormalName**: BOLSA ELECTRONICA DE VALORES DEL URUGUAY
- **hasWebsite**: https://web.bevsa.com.uy/bevsaintranet2008/inicio/default.aspx

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
