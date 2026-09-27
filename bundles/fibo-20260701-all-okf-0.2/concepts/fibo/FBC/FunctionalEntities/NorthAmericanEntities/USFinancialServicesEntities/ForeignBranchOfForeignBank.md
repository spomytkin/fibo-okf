---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: foreign branch of foreign bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: branch that resides outside of the United States whose parent is located outside of the United States
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticBranchOfDomesticBank.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticBranchOfDomesticBank
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBranchOfUSBank.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBranchOfUSBank
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
    value: N093001eb65b44bffb02e371185ce7b38
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Organizations/isDomiciledIn
    value: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BranchOfADepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BranchOfADepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBranchOfForeignBank
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: foreign branch of foreign bank
type: Ontology Class
---

# foreign branch of foreign bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBranchOfForeignBank>

## Definition

branch that resides outside of the United States whose parent is located outside of the United States

## Relationships

- **Subclass of**: [BranchOfADepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BranchOfADepositoryInstitution.md)

## Constraints

- **Disjoint with**: [DomesticBranchOfDomesticBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticBranchOfDomesticBank.md)
- **Disjoint with**: [ForeignBranchOfUSBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBranchOfUSBank.md)
- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from value `N093001eb65b44bffb02e371185ce7b38`
- **[isDomiciledIn](<https://www.omg.org/spec/Commons/Organizations/isDomiciledIn>)**: has value value `https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica`

## Annotations

- **label**: foreign branch of foreign bank
- **definition**: branch that resides outside of the United States whose parent is located outside of the United States

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
