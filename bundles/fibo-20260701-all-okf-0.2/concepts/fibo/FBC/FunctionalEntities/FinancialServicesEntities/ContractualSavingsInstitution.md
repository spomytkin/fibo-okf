---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual savings institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution that provides the opportunity for individuals to invest in collective investment vehicles
      in a fiduciary rather than a principle role
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Example institutional investors include banks, insurance companies, mutual funds, pension funds, and other similar
      large funds.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.worldbank.org/en/publication/gfdr/gfdr-2016/background/nonbank-financial-institution
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Collective investment vehicles invest the pooled resources of the individuals and firms into numerous equity, debt,
      and derivatives promises. The individual, however, holds equity in the CIV itself rather what the CIV invests in specifically.
      The two most popular examples of contractual savings institutions are mutual funds and private pension plans.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically more than 70 percent of the daily trading on the New York Stock Exchange is conducted on behalf of institutional
      investors.
  - language: en-US
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: institutional investment firm
  - language: en-US
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: institutional investor
  - language: fr-FR
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: investisseur institutionnel
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ContractualSavingsInstitution
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: contractual savings institution
type: Ontology Class
---

# contractual savings institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ContractualSavingsInstitution>

## Definition

financial institution that provides the opportunity for individuals to invest in collective investment vehicles in a fiduciary rather than a principle role

## Relationships

- **Subclass of**: [Investor](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md)
- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: min qualified cardinality 0

## Annotations

- **label**: contractual savings institution
- **definition**: financial institution that provides the opportunity for individuals to invest in collective investment vehicles in a fiduciary rather than a principle role
- **example**: Example institutional investors include banks, insurance companies, mutual funds, pension funds, and other similar large funds.
- **adaptedFrom**: https://www.worldbank.org/en/publication/gfdr/gfdr-2016/background/nonbank-financial-institution
- **explanatoryNote**: Collective investment vehicles invest the pooled resources of the individuals and firms into numerous equity, debt, and derivatives promises. The individual, however, holds equity in the CIV itself rather what the CIV invests in specifically. The two most popular examples of contractual savings institutions are mutual funds and private pension plans.
- **explanatoryNote**: Typically more than 70 percent of the daily trading on the New York Stock Exchange is conducted on behalf of institutional investors.
- **synonym** (en-US): institutional investment firm
- **synonym** (en-US): institutional investor
- **synonym** (fr-FR): investisseur institutionnel

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
