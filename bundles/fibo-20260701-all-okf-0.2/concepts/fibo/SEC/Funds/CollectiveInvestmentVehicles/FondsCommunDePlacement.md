---
owl:
  annotations:
  - language: fr-FR
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fonds commun de placement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: open-ended collective investment fund, which is a contractual form set up between the fund manager and investors
      and not a separate legal entity
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: An FCP is similar to a unit trust in the UK. FCPs are not investment companies, but more like open partnerships.
      They can be set up as a single fund or as an umbrella fund with multiple sub-funds, typically issued in the French-speaking
      countries of Europe.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FCP
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://iclg.com/practice-areas/public-investment-funds-laws-and-regulations/france
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.alfi.lu/en-gb/understandinginvesting/post/which-structure-to-choose
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.ubp.com/en/glossary-risk-management/glossary-legal-compliance/fcp
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FondsCommunDePlacement
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fonds commun de placement
type: Ontology Class
---

# fonds commun de placement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FondsCommunDePlacement>

## Definition

open-ended collective investment fund, which is a contractual form set up between the fund manager and investors and not a separate legal entity

## Relationships

- **See also**: [france](<https://iclg.com/practice-areas/public-investment-funds-laws-and-regulations/france>)
- **See also**: [which-structure-to-choose](<https://www.alfi.lu/en-gb/understandinginvesting/post/which-structure-to-choose>)
- **See also**: [fcp](<https://www.ubp.com/en/glossary-risk-management/glossary-legal-compliance/fcp>)
- **Subclass of**: [CollectiveInvestmentVehicle](/concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)

## Annotations

- **label** (fr-FR): fonds commun de placement
- **definition** (en): open-ended collective investment fund, which is a contractual form set up between the fund manager and investors and not a separate legal entity
- **note** (en): An FCP is similar to a unit trust in the UK. FCPs are not investment companies, but more like open partnerships. They can be set up as a single fund or as an umbrella fund with multiple sub-funds, typically issued in the French-speaking countries of Europe.
- **abbreviation** (en): FCP

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
