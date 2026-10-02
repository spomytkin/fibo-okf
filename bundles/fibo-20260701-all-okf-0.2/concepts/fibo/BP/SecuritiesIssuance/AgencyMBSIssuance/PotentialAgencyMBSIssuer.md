---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: potential agency m b s issuer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The entity which will become the issuing party for the pass through MBS Issue. This entity is the principal actor
      in most of the activities involved in the issue. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/AddMortgageToPool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/adds
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/FinalizePoolContent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/finalizes
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/IdentifyConformingMortgage
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/identifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/AcquireMortgage
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/purchases
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/ValidateConformance
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/validates
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/AssessPoolSuitablilityForIssuance
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/ClassifyMortgage
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PotentialAgencyMBSIssuer
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: potential agency m b s issuer
type: Ontology Class
---

# potential agency m b s issuer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PotentialAgencyMBSIssuer>

## Definition

The entity which will become the issuing party for the pass through MBS Issue. This entity is the principal actor in most of the activities involved in the issue. Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [PoolBackedSecuritySecuritizationProcessActor](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor.md)

## Constraints

- **[adds](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/adds.md)**: some values from of type [AddMortgageToPool](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/AddMortgageToPool.md)
- **[finalizes](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/finalizes.md)**: some values from of type [FinalizePoolContent](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/FinalizePoolContent.md)
- **[identifies](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/identifies.md)**: some values from of type [IdentifyConformingMortgage](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/IdentifyConformingMortgage.md)
- **[purchases](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/purchases.md)**: some values from of type [AcquireMortgage](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/AcquireMortgage.md)
- **[validates](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/validates.md)**: some values from of type [ValidateConformance](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/ValidateConformance.md)
- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: some values from of type [AssessPoolSuitablilityForIssuance](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/AssessPoolSuitablilityForIssuance.md)
- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: some values from of type [ClassifyMortgage](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/ClassifyMortgage.md)

## Annotations

- **label** (en): potential agency m b s issuer
- **definition** (en): The entity which will become the issuing party for the pass through MBS Issue. This entity is the principal actor in most of the activities involved in the issue. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
