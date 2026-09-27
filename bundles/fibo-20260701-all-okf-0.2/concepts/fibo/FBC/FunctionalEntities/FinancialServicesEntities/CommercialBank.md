---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commercial bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depository institution that engages in various financial services, such as accepting deposits and making loans
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A commercial bank is a financial institution that is owned by stockholders, operates for a profit, and engages
      in various lending activities. Commercial banks provide services, such as accepting deposits, giving business loans
      and auto loans, mortgage lending, and basic investment products like savings accounts and certificates of deposit.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The traditional commercial bank is a brick and mortar institution with tellers, safe deposit boxes, vaults and
      ATMs. However, some commercial banks do not have any physical branches and require consumers to complete all transactions
      by phone or Internet. In exchange, they generally pay higher interest rates on investments and deposits, and charge
      lower fees.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.ffiec.gov/nicpubweb/Content/HELP/Institution%20Type%20Description.htm
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Bank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: commercial bank
type: Ontology Class
---

# commercial bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank>

## Definition

depository institution that engages in various financial services, such as accepting deposits and making loans

## Relationships

- **See also**: [Institution%20Type%20Description.htm](<http://www.ffiec.gov/nicpubweb/Content/HELP/Institution%20Type%20Description.htm>)
- **Subclass of**: [Bank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [Corporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md)

## Annotations

- **label**: commercial bank
- **definition**: depository institution that engages in various financial services, such as accepting deposits and making loans
- **explanatoryNote**: A commercial bank is a financial institution that is owned by stockholders, operates for a profit, and engages in various lending activities. Commercial banks provide services, such as accepting deposits, giving business loans and auto loans, mortgage lending, and basic investment products like savings accounts and certificates of deposit.
- **explanatoryNote**: The traditional commercial bank is a brick and mortar institution with tellers, safe deposit boxes, vaults and ATMs. However, some commercial banks do not have any physical branches and require consumers to complete all transactions by phone or Internet. In exchange, they generally pay higher interest rates on investments and deposits, and charge lower fees.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
