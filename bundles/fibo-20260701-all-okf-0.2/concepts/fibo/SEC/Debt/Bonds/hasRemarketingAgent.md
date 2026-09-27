---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has remarketing agent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the dealer responsible for reselling to investors securities (such as variable rate demand obligations
      and other tender option bonds) that have been tendered for purchase by their owner.
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalSecurity
  range:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalDebtRemarketingAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalDebtRemarketingAgent
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasRemarketingAgent
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has remarketing agent
type: Ontology Property
---

# has remarketing agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasRemarketingAgent>

## Definition

identifies the dealer responsible for reselling to investors securities (such as variable rate demand obligations and other tender option bonds) that have been tendered for purchase by their owner.

## Relationships

- **Domain**: [MunicipalSecurity](/concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md)
- **Range**: [MunicipalDebtRemarketingAgent](/concepts/fibo/SEC/Debt/Bonds/MunicipalDebtRemarketingAgent.md)
- **Subproperty of**: [hasThirdParty](/concepts/fibo/FND/Agreements/Contracts/hasThirdParty.md)

## Annotations

- **label**: has remarketing agent
- **definition**: identifies the dealer responsible for reselling to investors securities (such as variable rate demand obligations and other tender option bonds) that have been tendered for purchase by their owner.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
