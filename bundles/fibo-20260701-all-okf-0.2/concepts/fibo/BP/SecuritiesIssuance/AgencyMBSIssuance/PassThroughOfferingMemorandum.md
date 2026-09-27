---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pass through offering memorandum
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The offering memorandum for a pass through MBS issue, setting out basic information about a future issue, for the
      information of prospective investors and their agents. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSFinalTermsheet
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MBSIssuance/includesDetailsAbout
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughOfferingMemorandum
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: pass through offering memorandum
type: Ontology Class
---

# pass through offering memorandum

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughOfferingMemorandum>

## Definition

The offering memorandum for a pass through MBS issue, setting out basic information about a future issue, for the information of prospective investors and their agents. Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [OfferingDocument](/concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)

## Constraints

- **[includesDetailsAbout](/concepts/fibo/BP/SecuritiesIssuance/MBSIssuance/includesDetailsAbout.md)**: some values from of type [PassThroughMBSFinalTermsheet](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSFinalTermsheet.md)

## Annotations

- **label** (en): pass through offering memorandum
- **definition** (en): The offering memorandum for a pass through MBS issue, setting out basic information about a future issue, for the information of prospective investors and their agents. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
