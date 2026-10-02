---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: potential non agency m b s issuer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The entity which will become the issuing party for the Tranched MBS Issue. This entity is the principal actor in
      most of the activities involved in the issue. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AssessPoolSuitabilityForIssuance
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AssessRatings
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PotentialNonAgencyMBSIssuer
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: potential non agency m b s issuer
type: Ontology Class
---

# potential non agency m b s issuer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PotentialNonAgencyMBSIssuer>

## Definition

The entity which will become the issuing party for the Tranched MBS Issue. This entity is the principal actor in most of the activities involved in the issue. Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [PoolBackedSecuritySecuritizationProcessActor](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor.md)

## Constraints

- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: some values from of type [AssessPoolSuitabilityForIssuance](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AssessPoolSuitabilityForIssuance.md)
- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: some values from of type [AssessRatings](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AssessRatings.md)

## Annotations

- **label** (en): potential non agency m b s issuer
- **definition** (en): The entity which will become the issuing party for the Tranched MBS Issue. This entity is the principal actor in most of the activities involved in the issue. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
