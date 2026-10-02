---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: municipal debt remarketing agent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: municipal securities dealer responsible for reselling to investors securities (such as variable rate demand obligations
      and other tender option bonds) that have been tendered for purchase by their owner
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The remarketing agent also typically is responsible for resetting the interest rate for a variable rate issue and
      may act as tender agent.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Dealer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Dealer
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalDebtRemarketingAgent
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: municipal debt remarketing agent
type: Ontology Class
---

# municipal debt remarketing agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalDebtRemarketingAgent>

## Definition

municipal securities dealer responsible for reselling to investors securities (such as variable rate demand obligations and other tender option bonds) that have been tendered for purchase by their owner

## Relationships

- **Subclass of**: [Dealer](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Dealer.md)
- **Subclass of**: [ContractThirdParty](/concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md)

## Annotations

- **label**: municipal debt remarketing agent
- **definition**: municipal securities dealer responsible for reselling to investors securities (such as variable rate demand obligations and other tender option bonds) that have been tendered for purchase by their owner
- **explanatoryNote**: The remarketing agent also typically is responsible for resetting the interest rate for a variable rate issue and may act as tender agent.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
