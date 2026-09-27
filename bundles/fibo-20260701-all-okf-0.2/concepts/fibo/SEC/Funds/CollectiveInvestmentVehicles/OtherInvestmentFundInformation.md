---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: other investment fund information
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Things which are not part of the prospectus but are important if you want to understand the fund.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'See terms in EFAMA spreadsheet. These are properties of the fund but are not legally binding. Author follow-up
      note: I have managed to find a "home" for disposition for most of the entries that are in the spreadsheet. It is not
      clear which of the spreadsheet terms are indended to come under the general heading in this class. The first place I
      would look is in the terms I have defined as "Fund Processing Terms", which are defined as formal, legal contractual
      terms. If any of those are not legally binding on some party, then this is where they belong instead.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Document
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/OtherInvestmentFundInformation
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: other investment fund information
type: Ontology Class
---

# other investment fund information

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/OtherInvestmentFundInformation>

## Definition

Things which are not part of the prospectus but are important if you want to understand the fund.

## Relationships

- **Subclass of**: [Document](<https://www.omg.org/spec/Commons/Documents/Document>)

## Annotations

- **label** (en): other investment fund information
- **definition** (en): Things which are not part of the prospectus but are important if you want to understand the fund.
- **editorialNote** (en): See terms in EFAMA spreadsheet. These are properties of the fund but are not legally binding. Author follow-up note: I have managed to find a "home" for disposition for most of the entries that are in the spreadsheet. It is not clear which of the spreadsheet terms are indended to come under the general heading in this class. The first place I would look is in the terms I have defined as "Fund Processing Terms", which are defined as formal, legal contractual terms. If any of those are not legally binding on some party, then this is where they belong instead.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
