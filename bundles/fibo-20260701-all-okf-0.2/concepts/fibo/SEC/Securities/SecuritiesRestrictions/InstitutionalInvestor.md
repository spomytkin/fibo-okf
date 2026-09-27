---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: institutional investor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investor that pools money to purchase securities, real property, and other investment assets or originates loans
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Institutional investors typically buy, sell, and manage stocks, bonds, and other investment securities on behalf
      of its clients, customers, members, or shareholders. These include endowment funds, commercial banks, mutual funds,
      hedge funds, pension funds, and insurance companies. Institutional investors are able to invest in riskier securities
      and ventures than average investors because they are more sophisticated with respect to their investment methodologies.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesRestrictions/IndividualInvestor.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/IndividualInvestor
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalEntity
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/InstitutionalInvestor
sources:
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: institutional investor
type: Ontology Class
---

# institutional investor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/InstitutionalInvestor>

## Definition

investor that pools money to purchase securities, real property, and other investment assets or originates loans

## Relationships

- **Subclass of**: [Investor](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md)

## Constraints

- **Disjoint with**: [IndividualInvestor](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/IndividualInvestor.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: all values from of type [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label**: institutional investor
- **definition**: investor that pools money to purchase securities, real property, and other investment assets or originates loans
- **explanatoryNote**: Institutional investors typically buy, sell, and manage stocks, bonds, and other investment securities on behalf of its clients, customers, members, or shareholders. These include endowment funds, commercial banks, mutual funds, hedge funds, pension funds, and insurance companies. Institutional investors are able to invest in riskier securities and ventures than average investors because they are more sophisticated with respect to their investment methodologies.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
