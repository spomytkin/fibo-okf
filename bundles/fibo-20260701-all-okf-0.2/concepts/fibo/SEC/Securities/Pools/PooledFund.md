---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pooled fund
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: pool of funds that a group of investors combines for common benefit
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: An investment club pools the funds of its members, giving them the opportunity to share in a portfolio offering
      greater diversification and the hope of a better return on their money than they could get individually.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The US Securities and Exchange Commission describes a fund as an entity created to pool money from multiple investors.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A fund can be established for any purpose, such as a municipality setting aside money for a construction project,
      monies designated to endow a university chair or for scholarships, or funds set aside by insurance companies to settle
      claims.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: fund
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: fund
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasDateEstablished
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/InvestmentObjective
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  - filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isPrivate
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasPart
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/private-funds
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
  - concept: /concepts/fibo/SEC/Securities/Pools/Pool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/Pool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: pooled fund
type: Ontology Class
---

# pooled fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund>

## Definition

pool of funds that a group of investors combines for common benefit

## Relationships

- **See also**: [private-funds](<https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/private-funds>)
- **Subclass of**: [FinancialAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md)
- **Subclass of**: [Pool](/concepts/fibo/SEC/Securities/Pools/Pool.md)

## Constraints

- **[hasDateEstablished](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/hasDateEstablished.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: some values from of type [InvestmentObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/InvestmentObjective.md)
- **[isPrivate](/concepts/fibo/SEC/Funds/Funds/isPrivate.md)**: all values from of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)**: some values from of type [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)

## Annotations

- **label**: pooled fund
- **definition**: pool of funds that a group of investors combines for common benefit
- **example**: An investment club pools the funds of its members, giving them the opportunity to share in a portfolio offering greater diversification and the hope of a better return on their money than they could get individually.
- **explanatoryNote**: The US Securities and Exchange Commission describes a fund as an entity created to pool money from multiple investors.
- **explanatoryNote** (en): A fund can be established for any purpose, such as a municipality setting aside money for a construction project, monies designated to endow a university chair or for scholarships, or funds set aside by insurance companies to settle claims.
- **synonym**: fund
- **synonym** (en): fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
