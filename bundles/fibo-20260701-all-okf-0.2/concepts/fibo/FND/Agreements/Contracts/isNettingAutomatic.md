---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is netting automatic
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether netting takes place automatically under the scope of the agreement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Example text: "If on any date amounts would otherwise be payable:- (i) in the same currency; and (ii) in respect
      of the same Transaction, by each party to the other, then, on such date, each party''s obligation to make payment of
      any such amount will be automatically satisfied and discharged and, if the aggregate amount that would otherwise have
      been payable by one party exceeds the aggregate amount that would otherwise have been payable by the other party, replaced
      by an obligation upon the party by whom the larger aggregate amount would have been payable to pay to the other party
      the excess of the larger aggregate amount over the smaller aggregate amount."'
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/NettingProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NettingProvision
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isNettingAutomatic
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: is netting automatic
type: Ontology Property
---

# is netting automatic

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isNettingAutomatic>

## Definition

indicates whether netting takes place automatically under the scope of the agreement

## Relationships

- **Domain**: [NettingProvision](/concepts/fibo/FND/Agreements/Contracts/NettingProvision.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is netting automatic
- **definition** (en): indicates whether netting takes place automatically under the scope of the agreement
- **example** (en): Example text: "If on any date amounts would otherwise be payable:- (i) in the same currency; and (ii) in respect of the same Transaction, by each party to the other, then, on such date, each party's obligation to make payment of any such amount will be automatically satisfied and discharged and, if the aggregate amount that would otherwise have been payable by one party exceeds the aggregate amount that would otherwise have been payable by the other party, replaced by an obligation upon the party by whom the larger aggregate amount would have been payable to pay to the other party the excess of the larger aggregate amount over the smaller aggregate amount."

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
