---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agency agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: agreement that designates a party as a registered agent to represent and act on behalf of another party in some,
      typically legal, financial, or medical capacity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.sos.state.tx.us/corp/registeredagents.shtml
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/AgencyAgreement
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: agency agreement
type: Ontology Class
---

# agency agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/AgencyAgreement>

## Definition

agreement that designates a party as a registered agent to represent and act on behalf of another party in some, typically legal, financial, or medical capacity

## Relationships

- **See also**: [registeredagents.shtml](<http://www.sos.state.tx.us/corp/registeredagents.shtml>)
- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [RegisteredAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md)

## Annotations

- **label**: agency agreement
- **definition**: agreement that designates a party as a registered agent to represent and act on behalf of another party in some, typically legal, financial, or medical capacity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
