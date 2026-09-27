---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Stock Exchange Daily Official List (SEDOL) scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: national security identification scheme used to identify all stocks and registered bonds in the United Kingdom
      for the purposes of facilitating clearing and settlement of trades
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SEDOL scheme
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentificationScheme
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme
  related_to:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/SEDOLMasterFile.md
    predicate: https://www.omg.org/spec/Commons/Designators/describes
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/SEDOLMasterFile
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.isin.net/sedol/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/StockExchangeDailyOfficialListScheme
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Stock Exchange Daily Official List (SEDOL) scheme
type: Ontology Individual
---

# Stock Exchange Daily Official List (SEDOL) scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/StockExchangeDailyOfficialListScheme>

## Definition

national security identification scheme used to identify all stocks and registered bonds in the United Kingdom for the purposes of facilitating clearing and settlement of trades

## Relationships

- **Related to**: [SEDOLMasterFile](/concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/SEDOLMasterFile.md)
- **See also**: [sedol](<https://www.isin.net/sedol/>)

## Annotations

- **label**: Stock Exchange Daily Official List (SEDOL) scheme
- **definition**: national security identification scheme used to identify all stocks and registered bonds in the United Kingdom for the purposes of facilitating clearing and settlement of trades
- **abbreviation**: SEDOL scheme

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
