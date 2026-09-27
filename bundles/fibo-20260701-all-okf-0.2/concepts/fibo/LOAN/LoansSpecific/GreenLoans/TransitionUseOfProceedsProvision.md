---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transition use of proceeds provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: use of proceeds provision specifying that funds obtained through financing, such as through a credit agreement,
      offering, warrant, or other instrument are intended to be used to fund specific projects, investments, or operational
      changes that support a company's transition toward sustainability
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionProject
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/UseOfProceedsProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/UseOfProceedsProvision
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionUseOfProceedsProvision
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: transition use of proceeds provision
type: Ontology Class
---

# transition use of proceeds provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionUseOfProceedsProvision>

## Definition

use of proceeds provision specifying that funds obtained through financing, such as through a credit agreement, offering, warrant, or other instrument are intended to be used to fund specific projects, investments, or operational changes that support a company's transition toward sustainability

## Relationships

- **Subclass of**: [UseOfProceedsProvision](/concepts/fibo/FND/Agreements/Contracts/UseOfProceedsProvision.md)

## Constraints

- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [TransitionProject](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/TransitionProject.md)

## Annotations

- **label**: transition use of proceeds provision
- **definition**: use of proceeds provision specifying that funds obtained through financing, such as through a credit agreement, offering, warrant, or other instrument are intended to be used to fund specific projects, investments, or operational changes that support a company's transition toward sustainability

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
