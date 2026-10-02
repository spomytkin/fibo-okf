---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tranched offering memorandum
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The Offering Memorandum will include or attach the terms for two or more individual tranches that will make up
      the issue, and the structure of the tranches, including how they will relate to one another (priorities and so on).
      Term origin:MBS PoC Reviews
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The offering memorandum for a tranched MBS issue, setting out basic information about a future issue, for the information
      of prospective investors and their agents.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TrancheStructureAndTermsheet
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/includesDetailsAbout
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/IndividualTrancheDefinitions
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/includesDetailsAbout.1
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/DraftTrancheNotesParameters
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/mayIncludeDetailsAbout
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedOfferingMemorandum
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: tranched offering memorandum
type: Ontology Class
---

# tranched offering memorandum

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedOfferingMemorandum>

## Definition

The offering memorandum for a tranched MBS issue, setting out basic information about a future issue, for the information of prospective investors and their agents.

## Additional definitions

- The Offering Memorandum will include or attach the terms for two or more individual tranches that will make up the issue, and the structure of the tranches, including how they will relate to one another (priorities and so on). Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [OfferingDocument](/concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)

## Constraints

- **[includesDetailsAbout](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/includesDetailsAbout.md)**: some values from of type [TrancheStructureAndTermsheet](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TrancheStructureAndTermsheet.md)
- **[includesDetailsAbout.1](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/includesDetailsAbout.1.md)**: some values from of type [IndividualTrancheDefinitions](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/IndividualTrancheDefinitions.md)
- **[mayIncludeDetailsAbout](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/mayIncludeDetailsAbout.md)**: max qualified cardinality 1 of type [DraftTrancheNotesParameters](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/DraftTrancheNotesParameters.md)

## Annotations

- **label** (en): tranched offering memorandum
- **definition** (en): The Offering Memorandum will include or attach the terms for two or more individual tranches that will make up the issue, and the structure of the tranches, including how they will relate to one another (priorities and so on). Term origin:MBS PoC Reviews
- **definition** (en): The offering memorandum for a tranched MBS issue, setting out basic information about a future issue, for the information of prospective investors and their agents.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
