---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government mortgage agency
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An agency set up by a government for the purpose of issuing mortgages.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: 'There are three such agencies in the United States: FNMA, GNMA and FHLMC (Fannie Mae, Ginnie Mae and Freddie Mac
      respectively), and there may be others outside of the US.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalEntity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/GovernmentMortgageAgency
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: government mortgage agency
type: Ontology Class
---

# government mortgage agency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/GovernmentMortgageAgency>

## Definition

An agency set up by a government for the purpose of issuing mortgages.

## Relationships

- **Subclass of**: [FunctionalEntity](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label** (en): government mortgage agency
- **definition** (en): An agency set up by a government for the purpose of issuing mortgages.
- **scopeNote** (en): There are three such agencies in the United States: FNMA, GNMA and FHLMC (Fannie Mae, Ginnie Mae and Freddie Mac respectively), and there may be others outside of the US.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
